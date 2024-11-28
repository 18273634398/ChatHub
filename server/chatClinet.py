

from openai import OpenAI
import requests
from control import settings,checkSystem
from server.model import  DeepSeekModel,KimiModel,ZeroOneModel,BigModel,templateModel
modelList = [None,BigModel.BigModel(),DeepSeekModel.DeepSeekModel(),ZeroOneModel.ZeroOneModel(),KimiModel.KimiModel()]

# 用于单论对话
def chat_init(text,model):
    # 初始化API
    client = OpenAI(api_key=model.api_key, base_url=model.base_url)
    # 提示词工程
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": text},
    ]
    # 调用API进行对话
    response = client.chat.completions.create(
        model=model.model,
        messages=messages,
        stream=True,
        tools=model.tools
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
    return messages


# 用于多轮对话进行回复
def chat(text,messages,model):
    # 文本检查
    checkSystem.input_check(text)
    try:
        # 进行model对象转化
        if not isinstance(model,templateModel.TemplateModel):
            model = modelList[int(model)]
        if messages == None:
            messages = chat_init(text,model)
        else:
            print(f"前后对话记录：{messages}")
            client = OpenAI(api_key=model.api_key, base_url=model.base_url)
            response = client.chat.completions.create(
                model=model.model,
                messages=messages,
                stream=True
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

        # 启动第二轮对话
        text = input("\n"+settings.user_name+": ")
        chat(text,messages,model)
    except Exception as e:
        print(f"Error,错误信息：{e}")



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


