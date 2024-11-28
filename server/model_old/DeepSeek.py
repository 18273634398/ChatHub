from openai import OpenAI
from control.settings import showApiUsage, deepSeek_balance_url,deepSeek_api_key, deepSeek_base_url, assistant_name,user_name
import requests

# 定义模型
model = "deepseek-chat"
api_key = deepSeek_api_key
base_url = deepSeek_base_url
balance_url = deepSeek_balance_url

# 用于单论对话
def chat_init(text):
    # 初始化API
    client = OpenAI(api_key=api_key, base_url=base_url)
    # 提示词工程
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": text},
    ]
    # 调用API进行对话
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True
    )
    # Chat流式回复响应
    chatTempResponse = {"role": "assistant", "content":"" }
    print(assistant_name+":",end='')
    for chunk in response:
        content = chunk.choices[0].delta.content
        print(content,end='')
        chatTempResponse["content"] += content
        if showApiUsage and chunk.usage:
            print("\n[本次调用已使用 API 配额: "+str(chunk.usage.total_tokens)+" tokens],剩余配额:"+str(check_balance()))
    messages.append(chatTempResponse)
    return messages


# 用于多轮对话进行回复
def chat(text,messages):
    try:
        if messages == None:
            messages = chat_init(text)
            print(f"前后对话记录：{messages}")
        else:
            client = OpenAI(api_key=api_key, base_url=base_url)
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True
            )
            print(assistant_name+":",end='')
            chatTempResponse = {"role": "assistant", "content":"" }
            for chunk in response:
                content = chunk.choices[0].delta.content
                print(content,end='')
                chatTempResponse["content"] += content
                if showApiUsage and chunk.usage:
                    print("\n[本次调用已使用 API 配额: "+str(chunk.usage.total_tokens)+" tokens],剩余配额:"+str(check_balance()))
            messages.append(chatTempResponse)

        # 启动第二轮对话
        text = input(user_name+": ")
        chat(text,messages)
    except Exception as e:
        print(f"Error:请检查API Key是否正确！,错误信息：{e}")

# Check API Key Balance
# Return:
#   isAvailable: API Key是否可用
#   balance: API Key余额
def check_balance():
    url = balance_url
    payload={}
    headers = {
        'Accept': 'application/json',
        'Authorization': "Bearer "+api_key
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