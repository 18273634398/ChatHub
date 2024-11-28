from control.settings import bigModel_api_key, bigModel_base_url
from server.model.templateModel import TemplateModel


class BigModel(TemplateModel):
    def __init__(self):
        super().__init__()
        self.model = "glm-4"
        self.api_key = bigModel_api_key
        self.base_url = bigModel_base_url
        self.balance_url = None
        self.tools = None
