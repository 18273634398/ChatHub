# Global Settings
user_name = "Input"
assistant_name = "Output"
max_tokens = 4096
showApiUsage = True


# API Manager
# DeepSeek Manager
deepSeek_api_key = "sk-0a234aa7065d46c0b0630b49f5ae8cbe"
deepSeek_base_url = "https://api.deepseek.com"
deepSeek_balance_url = "https://api.deepseek.com/user/balance"
def update_deepSeek_api_key(new_key):
    global deepSeek_api_key
    deepSeek_api_key = new_key


# BigModel Manager
bigModel_api_key = "db3cc1824946bbe99fc4a88e7bbb9a9d.G9tBherinRMdTuJv"
bigModel_base_url = "https://open.bigmodel.cn/api/paas/v4/"
def update_bigModel_api_key(new_key):
    global bigModel_api_key
    bigModel_api_key = new_key


# LingYiWanWu Manager
ZeroOne_api_key = "561d66cc66ed4f81958c281f8d12322c"
ZeroOne_base_url = "https://api.lingyiwanwu.com/v1"
def update_zeroOne_base_api_key(new_key):
    global ZeroOne_api_key
    ZeroOne_api_key = new_key

# Kimi Manager
Kimi_api_key = "sk-qWf5B76ID9IQfxGRkGoF7K5Qh3oa5PwXAuBtyzXIk7pUjOSb"
Kimi_base_url = "https://api.moonshot.cn/v1"
Kimi_notice ="[客户端通知] Kimi官方限制了调用速率，清尽量减少使用该模型。。"