from .State import State


class SettingBackground(State):
    def document_received(self, document):
        self.model.background = document
        self.model.events.background_set()

    def stateInit(self):
        self.model.clear_data()
        self.send_message("Welcome to the AOE Shirtbot! send /help for help")
        self.send_message("Send the background Image of your post")
        