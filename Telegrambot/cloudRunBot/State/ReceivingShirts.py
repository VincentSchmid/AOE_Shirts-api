from typing import Any
from .State import State


class ReceivingShirts(State):
    def document_received(self, document: Any):
        self.model.shirts.append(document)
        self.send_message(self.options["APP"]["RECIEVE_SHIRT"]["ON_DOCUMENT"])

    def stateInit(self):
        self.send_message(self.options["APP"]["RECIEVE_SHIRT"]["INIT"])

    def done_handler(self):
        if (self.model.id != None):
            self.send_message(self.options["APP"]["RECIEVE_SHIRT"]["DONE"])
            self.model.events.shirts_received()
        else:
            self.send_message(self.options["APP"]["RETURN_RESULT"]["INIT"])
