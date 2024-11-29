from control import System


def input_check(text,model):
    if text == "exit":
        System.Stop()
        exit()
    elif text =="update" or text == "updateKey" or text == "update_key" or text == "update_api_key" or text == "更新密钥":
        inputKey = input("[客户端] 请输入新的密钥：")
        model.update_api_key(inputKey)
        System.Restart()
    elif text == "restart" or text =="Restart" or text == "重启":
        System.Restart()
    else:
        return True

