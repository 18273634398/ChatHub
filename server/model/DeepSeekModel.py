from control.settings import deepSeek_api_key, deepSeek_base_url, deepSeek_balance_url
from server.model.templateModel import TemplateModel


class DeepSeekModel(TemplateModel):
    def __init__(self):
        super().__init__()
        self.model = "deepseek-chat"
        self.api_key = deepSeek_api_key
        self.base_url = deepSeek_base_url
        self.balance_url = deepSeek_balance_url
        self.tools = None
