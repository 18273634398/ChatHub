from time import sleep

def input_check(text):
    if text == "exit":
        print("正在退出系统，欢迎下次使用")
        sleep(1)
        exit()