from control.settings import ChatGPT_api_key, ChatGPT_base_url
from server.model.templateModel import TemplateModel


class ChatGPTModel(TemplateModel):
    def __init__(self):
        super().__init__()
        self.model = "gpt-4o-mini"
        self.api_key = ChatGPT_api_key
        self.base_url = ChatGPT_base_url
        self.balance_url = None
        self.tools = None