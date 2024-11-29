from control.settings import BaiChuan_api_key, BaiChuan_base_url
from server.model.templateModel import TemplateModel


class BaiChuanModel(TemplateModel):
    def __init__(self):
        super().__init__()
        self.model = "Baichuan4-Turbo"
        self.api_key = BaiChuan_api_key
        self.base_url = BaiChuan_base_url
        self.balance_url = None
        self.tools = None
        self.Prompt = ("你作为一名人工智能助手，相较于其他的智能助手你具有很强大的联网实时处理能力，因此你能够帮助用户处理各种各样的"
                       "实时问题，比如用户可能问你今天长沙的天气怎么样，你应该根据你在网络上实时获取的天气数据并迅速回复用户，这是你的巨大"
                       "优势，你必须充分发挥。")