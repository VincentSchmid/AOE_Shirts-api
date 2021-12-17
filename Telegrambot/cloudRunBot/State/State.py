from Model import AppModel


class State():
    def __init__(self, appModel: AppModel, options: dict):
        self.model = appModel
        self.options: dict = options
        self.stateInit()

    def document_received(self, document):
        self.send_error(self.options["APP"]["ERROR"]["FILES"])

    def stateInit(self):
        pass

    def start_handler(self):
        self.model.events.started()

    def done_handler(self):
        self.send_error(self.options["APP"]["ERROR"]["DONE"])

    def send_message(self, text):
        self.model.message = text
        self.model.events.send_message()

    def send_error(self, unexpected_type):
        generic_error_message = self.options["APP"]["ERROR"]["UNEXPECTED_TYPE"]
        error_message = generic_error_message.replace(
            self.options["SYNTAX"]["PLACEHOLDER"], unexpected_type, 1)
        self.send_message(error_message)
