from control import System


def input_check(text,model):
    if text == "exit":
        System.Stop()
        exit()
    elif text =="update" or text =="updateKey" or text =="update_key" or text =="update_api_key":
        inputKey = input("请输入新的密钥：")
        model.update_api_key(inputKey)
        System.Restart()
    else:
        return True

