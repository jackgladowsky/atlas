from atlas.model import ChatModel

class BaseAgent:
    def __init__(self, model: ChatModel):
        self.model = model

    def run(self):
        self.model.run()

