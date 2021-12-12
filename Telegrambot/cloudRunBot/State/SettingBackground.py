from .State import State
import uuid
from Model import AppModel


class SettingBackground(State):
    def document_received(self, document):
        self.model.background = document
        self.model.id = uuid.uuid4()
        self.model.events.background_set()

    def stateInit(self):
        AppModel.Get(self.chat_id).clear_data()
        self.send_message("Welcome to the AOE Shirtbot! send /help for help")
        self.send_message("Send the background Image of your post")
        