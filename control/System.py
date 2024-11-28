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
