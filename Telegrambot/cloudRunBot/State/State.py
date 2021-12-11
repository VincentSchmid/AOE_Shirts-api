from Model import AppModel


class State():
    def __init__(self, appModel: AppModel):
        self.model = appModel
        self.stateInit()

    def document_received(self, document):
        pass

    def stateInit(self):
        pass

    def start_handler(self):
        pass

    def done_handler(self):
        pass

    def send_message(self, text):
        self.model.message = text
        self.model.events.send_message()
