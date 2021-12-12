from Model import AppModel


class State():
    def __init__(self, appModel: AppModel):
        self.model = appModel
        self.stateInit()

    def document_received(self, document):
        self.send_message("Not Expecting files in this step, or maybe something went wrong?? Anyway send /start to restart the process")

    def stateInit(self):
        pass

    def start_handler(self):
        self.model.events.started()

    def done_handler(self):
        pass

    def send_message(self, text):
        self.model.message = text
        self.model.events.send_message()
