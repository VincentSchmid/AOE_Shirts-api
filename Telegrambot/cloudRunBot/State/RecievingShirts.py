from .State import State


class RecievingShirts(State):
    def document_received(self, document):
        self.model.shirts.append(document)
        self.send_message("Shirt received")

    def stateInit(self):
        self.send_message("Send Unedited Shirt Photos, after all the shirts were added send /done")

    def done_handler(self):
        if (self.model.id != None):
            self.send_message("Received shirts, now processing...")
            self.model.events.shirts_received()
        else:
            self.send_message("done")
            self.send_message("Send /start if you want to process more shirts")
