from control.settings import DeepSeek_api_key, DeepSeek_base_url, DeepSeek_balance_url
from server.model.templateModel import TemplateModel


class DeepSeekModel(TemplateModel):
    def __init__(self):
        super().__init__()
        self.model = "deepseek-chat"
        self.api_key = DeepSeek_api_key
        self.base_url = DeepSeek_base_url
        self.balance_url = DeepSeek_balance_url
        self.tools = None
