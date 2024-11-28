from server.model_old.BigModel import chat
from control.settings import user_name
message = input("Welcome to chatHub!now type your question\n"+user_name+": ")
chat(message,None)