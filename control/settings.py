# Global Settings
user_name = "Input"
assistant_name = "Output"
max_tokens = 4096
showApiUsage = False
longConversation = True
showHistory = False
# 提示词
Prompt = ("你是一个精通各种领域的智能助手，通过多次的学习训练，你已经掌握了很多技能，因此你可以为用户解决各种各样的问题，若用户提问你是谁等与你的身份相关的问题，请你回答：'我是有吾助手，我的开发者是鲁尚武，我支持很多技能，有什么可以帮你的吗？'")
# 运行中提示词开关
haveIntervalPrompt = False
# 运行中提示词
IntervalPrompt = {"role":"system","content":"请你分析用户最近的一次提问是否与之前的问题相关，若不相关，你只需要回复最新的问题即可，"
                                          "无需考虑之前的问题；若用户最近的一次问题与之前的问题相关，请你继续考虑之前的问答并做出回答。"}



# API Manager
# DeepSeek Manager
deepSeek_api_key = "sk-0a234aa7065d46c0b0630b49f5ae8cbe"
deepSeek_base_url = "https://api.deepseek.com"
deepSeek_balance_url = "https://api.deepseek.com/user/balance"
deepSeek_model_notice = "[客户端通知] 欢迎使用DeepSeek模型"


# BigModel Manager
bigModel_api_key = "db3cc1824946bbe99fc4a88e7bbb9a9d.G9tBherinRMdTuJv"
bigModel_base_url = "https://open.bigmodel.cn/api/paas/v4/"
big_model_notice = "[客户端通知] 欢迎使用BigModel模型"


# LingYiWanWu Manager
ZeroOne_api_key = "561d66cc66ed4f81958c281f8d12322c"
ZeroOne_base_url = "https://api.lingyiwanwu.com/v1"
zeroOne_model_notice = "[客户端通知] 欢迎使用零一万物模型"

# Kimi Manager
Kimi_api_key = "sk-qWf5B76ID9IQfxGRkGoF7K5Qh3oa5PwXAuBtyzXIk7pUjOSb"
Kimi_base_url = "https://api.moonshot.cn/v1"
Kimi_model_notice ="[客户端通知] Kimi官方限制了调用速率，清尽量减少使用该模型。。"