class TemplateModel:
    def __init__(self):
        self.model = None
        self.api_key = None
        self.Prompt = None

    def update_api_key(self,new_key):
        self.api_key = new_key
