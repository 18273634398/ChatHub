from server.chatClinet import chat
from control.settings import user_name
from control.settings import Kimi_notice
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
message = input("Welcome to chatHub!now type your question\n"+user_name+": ")
if select == '1':
    chat(message, None,1)
elif select == '2':
    chat(message, None,2)
elif select == '3':
    chat(message, None,3)
elif select == '4':
    print(Kimi_notice)
    chat(message, None,4)
else:
    print("Invalid selection, please try again.")