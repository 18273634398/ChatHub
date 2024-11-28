from control.settings import ZeroOne_base_url, ZeroOne_api_key
from server.model.templateModel import TemplateModel


class ZeroOneModel(TemplateModel):
    def __init__(self):
        super().__init__()
        self.model = "yi-lightning"
        self.base_url = ZeroOne_base_url
        self.api_key = ZeroOne_api_key
        self.balance_url = None
        self.tools = None