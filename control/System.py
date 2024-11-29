from time import sleep



def Stop():
    print("正在退出系统，欢迎下次使用")
    sleep(1)
    exit()

def Error(text):
    print(f"系统运行错误，错误信息：{text}, 正在退出系统")
    sleep(1)
    exit()

def Restart():
    print("正在重启系统，请等待...")
    sleep(1)
    Start()

def Start():
    from control.settings import Kimi_model_notice, deepSeek_model_notice, zeroOne_model_notice, big_model_notice
    from control.settings import user_name
    from server.chatClinet import chat

    DEFAULT_MODEL = 2

    hintText = '''
Welcome to the chatbot!
    Now please select a model_old:
        1. Big Model(智谱大模型GLM-4-Plus)
        2. DeepSeek Model(深度求索)
        3. ZeroOne Model(零一万物模型)
        4. Kimi Model(月影模型)
Input:
'''

    select = input(hintText)
    if select == '1':
        message = input(big_model_notice+"\n"+user_name+": ")
        chat(message, None,1)
    elif select == '2':
        message = input(deepSeek_model_notice+"\n"+user_name+": ")
        chat(message, None,2)
    elif select == '3':
        message = input(zeroOne_model_notice+"\n"+user_name+": ")
        chat(message, None,3)
    elif select == '4':
        message = input(Kimi_model_notice+"\n"+user_name+": ")
        print(Kimi_model_notice)
        chat(message, None,4)
    else:
        message = input("[客户端通知] 选择模型错误，使用默认模型\n"+user_name+": ")
        chat(message, None,DEFAULT_MODEL)




