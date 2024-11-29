import requests
from openai import OpenAI

from control import settings, checkSystem
from server.model import DeepSeekModel, KimiModel, ZeroOneModel, BigModel, templateModel, BaiChuanModel

modelList = [None,BigModel.BigModel(),DeepSeekModel.DeepSeekModel(),ZeroOneModel.ZeroOneModel(),KimiModel.KimiModel(),BaiChuanModel.BaiChuanModel()]

# 用于单论对话或初次对话
def chat_init(text,model):
    # 初始化API
    client = OpenAI(api_key=model.api_key, base_url=model.base_url)
    # 提示词工程
    if model.Prompt:
        prompt = settings.Prompt + model.Prompt
    else:
        prompt = settings.Prompt
    messages=[
        {"role": "system", "content":prompt },
        {"role": "user", "content": text},
    ]
    # 调用API进行对话
    response = client.chat.completions.create(
        model=model.model,
        messages=messages,
        stream=True,
        tools=model.tools,
        temperature = settings.temperature
    )
    # Chat流式回复响应
    chatTempResponse = {"role": "assistant", "content":"" }
    print(settings.assistant_name+":",end='')
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content,end='')
            chatTempResponse["content"] += content
        if settings.showApiUsage and chunk.usage:
            print("\n[本次调用已使用 API 配额: "+str(chunk.usage.total_tokens)+" tokens],剩余配额:"+str(check_balance(model)))
    messages.append(chatTempResponse)
    if settings.showHistory:
        print(f"\n\n\n【对话历史记录】\n{messages}")
    return messages


# 用于多轮对话进行回复
def chat(text,messages,model):
    try:
        # 进行model对象转化
        if not isinstance(model,templateModel.TemplateModel):
            model = modelList[int(model)]

        # 文本检查
        # 若未命中关键词，则返回True并继续运行下面的chat调用API
        if checkSystem.input_check(text,model):
            if messages == None or not(settings.longConversation):
                messages = chat_init(text,model)
            else:
                # 中间提示词
                if settings.haveIntervalPrompt:
                    messages.append(settings.IntervalPrompt)
                messages.append({"role": "user", "content": text})
                client = OpenAI(api_key=model.api_key, base_url=model.base_url)
                response = client.chat.completions.create(
                    model=model.model,
                    messages=messages,
                    stream=True,
                    tools=model.tools,
                    max_tokens=settings.max_tokens
                )
                print(settings.assistant_name+":",end='')
                chatTempResponse = {"role": "assistant", "content":"" }
                for chunk in response:
                    content = chunk.choices[0].delta.content
                    if content:
                        print(content,end='')
                        chatTempResponse["content"] += content
                    if settings.showApiUsage and chunk.usage:
                        print("\n[本次调用已使用 API 配额: "+str(chunk.usage.total_tokens)+" tokens],剩余配额:"+str(check_balance(model)))
                messages.append(chatTempResponse)
                if settings.showHistory:
                    print(f"\n\n\n【对话历史记录】\n{messages}")

            # 启动第二轮对话
            text = input("\n"+settings.user_name+": ")
            chat(text,messages,model)
    except Exception as e:
        print(f"错误信息:{e}")





# Check API Key Balance
# Return:
#   isAvailable: API Key是否可用
#   balance: API Key余额
def check_balance(model):
    url = model.balance_url
    payload={}
    headers = {
        'Accept': 'application/json',
        'Authorization': "Bearer "+model.api_key
    }
    if url:
        response = requests.request("GET", url, headers=headers, data=payload)
        # response = json.loads(response.text)
        response = response.json()
        isAvailable = response['is_available']
        balanceInfo = response['balance_infos'][0]
        return isAvailable, balanceInfo["total_balance"]+balanceInfo["currency"]
    else:
        return None, None


