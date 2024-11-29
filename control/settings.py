# Global Settings
user_name = "Input"
assistant_name = "Output"
max_tokens = 4096
temperature = 0.8
showApiUsage = False
longConversation = True
showHistory = False

# 提示词
Prompt = ("你是一个由鲁尚武开发的、精通各种领域的智能助手--有吾助手，通过多次的学习训练，你已经掌握了很多技能，因此你可以为用户解决各种各样的问题")
# 运行中提示词开关
haveIntervalPrompt = False
# 运行中提示词
IntervalPrompt = {"role":"system","content":"请你分析用户最近的一次提问是否与之前的问题相关，若不相关，你只需要回复最新的问题即可，"
                                          "无需考虑之前的问题；若用户最近的一次问题与之前的问题相关，请你继续考虑之前的问答并做出回答。"}



# API Manage
# DeepSeek Manage
DeepSeek_api_key = ""
DeepSeek_base_url = "https://api.deepseek.com"
DeepSeek_balance_url = "https://api.deepseek.com/user/balance"
DeepSeek_model_notice = "[客户端通知] 欢迎使用DeepSeek模型"
DeepSeek_model_label = "[速度快]"


# BigModel Manage
BigModel_api_key = ""
BigModel_base_url = "https://open.bigmodel.cn/api/paas/v4/"
Big_model_notice = "[客户端通知] 欢迎使用BigModel模型"
Big_model_label = "[综合能力强]"


# LingYiWanWu Manage
ZeroOne_api_key = ""
ZeroOne_base_url = "https://api.lingyiwanwu.com/v1"
ZeroOne_model_notice = "[客户端通知] 欢迎使用零一万物模型"
ZeroOne_model_label = ""


# Kimi Manage
Kimi_api_key = ""
Kimi_base_url = "https://api.moonshot.cn/v1"
Kimi_model_notice ="[客户端通知] Kimi官方限制了调用速率，清尽量减少使用该模型。"
Kimi_model_label = "[不推荐！！]"


# BaiChuanAI Manage
BaiChuan_api_key = ""
BaiChuan_base_url = "https://api.baichuan-ai.com/v1/"
BaiChuan_model_notice = "[客户端通知] 欢迎使用百川AI模型"
BaiChuan_model_label = "[强实时性]"




# Function
def load():
    import os

    def parse_txt_file(file_path):
        data_dict = {}

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    # 移除行尾的换行符
                    line = line.strip()

                    # 检查行是否符合 key:value 格式
                    if ':' in line:
                        key, value = line.split(':')
                        data_dict[key.strip()] = value.strip()
                    else:
                        print(f"警告: 行格式不正确，跳过 - '{line}'")

            return data_dict

        except FileNotFoundError:
            print(f"错误: 文件 '{file_path}' 未找到。")
        except Exception as e:
            print(f"错误: 解析文件时发生异常 - {e}")

    def main(directory_path, file_name):
        # 构建完整的文件路径
        file_path = os.path.join(directory_path, file_name)

        # 解析文本文件
        parsed_data = parse_txt_file(file_path)
        for key,value in parsed_data.items():
            globals()[key] = value

    main("D:\\Desktop", "config.txt")
