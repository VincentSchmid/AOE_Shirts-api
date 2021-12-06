from State import State


class RecievingShirts(State):
    def document_received(self, document):
        self.shirts.append(document)

    def stateInit(self):
        self.send_message("Send Unedited Shirt Photos, after all the shirts were added send /done")

    def done_handler(self):
        self.model.events.shirts_received()
    