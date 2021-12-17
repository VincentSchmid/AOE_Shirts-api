from typing import Any
from .State import State
import uuid


class SettingBackground(State):
    def document_received(self, document: Any):
        self.model.background = document
        self.model.id = uuid.uuid4()
        self.model.events.background_set()

    def stateInit(self):
        self.model.clear_data()
        self.send_message(self.options["APP"]["SETTING_BACKGROUND"]["INIT"])
        