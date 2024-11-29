from control.settings import BigModel_api_key, BigModel_base_url
from server.model.templateModel import TemplateModel


class BigModel(TemplateModel):
    def __init__(self):
        super().__init__()
        self.model = "glm-4"
        self.api_key = BigModel_api_key
        self.base_url = BigModel_base_url
        self.balance_url = None
        self.tools = None
