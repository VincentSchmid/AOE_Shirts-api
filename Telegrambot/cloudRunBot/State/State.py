from Model import AppModel


class State():
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.stateInit()

    def document_received(self, document):
        self.send_message("Not expecting files in this step, or maybe something went wrong?? Anyway send /start to restart the process")


    def stateInit(self):
        pass

    def start_handler(self):
        AppModel.Get(self.chat_id).events.started()

    def done_handler(self):
        self.send_message("Not expecting done command in this step, or maybe something went wrong?? Anyway send /start to restart the process")

    def send_message(self, text):
        model = AppModel.Get(self.chat_id)
        model.message = text
        model.events.send_message()
