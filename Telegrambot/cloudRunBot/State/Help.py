from .State import State


class Help(State):
    def stateInit(self):
        self.model.clear_data()
        self.send_message(self.options["APP"]["HELP"]["MESSAGE"])
