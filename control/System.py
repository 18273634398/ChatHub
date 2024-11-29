from time import sleep

from control.settings import load


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
    load()  # 加载配置 必须优先加载运行
    from control  import settings
    from control.settings import user_name
    from server.chatClinet import chat
    DEFAULT_MODEL = 2

    hintText = f'''
Welcome to the chatbot!
    Now please select a model_old:
        1. Big Model(智谱大模型GLM-4-Plus) {settings.Big_model_label}
        2. DeepSeek Model(深度求索)  {settings.DeepSeek_model_label}
        3. ZeroOne Model(零一万物模型)  {settings.ZeroOne_model_label}
        4. Kimi Model(月影模型)  {settings.Kimi_model_label}
        5. BaiChuan Model(百川模型)  {settings.BaiChuan_model_label}
Input:
'''

    select = input(hintText)
    if select == '1':
        message = input(settings.Big_model_notice + "\n" + user_name + ": ")
        chat(message, None,1)
    elif select == '2':
        message = input(settings.DeepSeek_model_notice + "\n" + user_name + ": ")
        chat(message, None,2)
    elif select == '3':
        message = input(settings.ZeroOne_model_notice + "\n" + user_name + ": ")
        chat(message, None,3)
    elif select == '4':
        message = input(settings.Kimi_model_notice+"\n"+user_name+": ")
        chat(message, None,4)
    elif select == '5':
        message = input(settings.BaiChuan_model_notice+"\n"+user_name+": ")
        chat(message, None,5)
    else:
        message = input("[客户端通知] 选择模型错误，使用默认模型\n"+user_name+": ")
        chat(message, None,DEFAULT_MODEL)






