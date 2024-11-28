from openai import OpenAI
from control.settings import *



# 定义参数
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
        model = model,
        messages = messages,
        stream = True,
        max_tokens = max_tokens
    )

    # Chat流式回复响应
    chatTempResponse = {"role": "assistant", "content":"" }
    print(assistant_name+":",end='')
    for chunk in response:
        content = chunk.choices[0].delta.content
        print(content,end='')
        chatTempResponse["content"] += content
        if chunk.usage:
            print("\n[本次调用已使用 API 配额: "+str(chunk.usage.total_tokens)+" tokens]")
    messages.append(chatTempResponse)
    return messages


# 用于多轮对话进行回复
def chat(text,messages):
    if messages == None:
        messages = chat_init(text)
        text = input(user_name+": ")
        chat(text,messages)
    else:
        client = OpenAI(api_key=api_key, base_url=base_url)
        messages.append({"role": "user", "content": text})
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
            if chunk.usage:
                print("\n[本次调用已使用 API 配额: "+str(chunk.usage.total_tokens)+" tokens]")
        messages.append(chatTempResponse)

        # 启动第二轮对话
        text = input(user_name+": ")
        chat(text,messages)

