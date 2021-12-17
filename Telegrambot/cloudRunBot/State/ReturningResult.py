from .State import State


class ReturningResult(State):
    def stateInit(self):
        self.model.id = None
        self.model.events.return_results()
    
    def done_handler(self):
        self.send_message(self.options["APP"]["RETURN_RESULT"]["INIT"])
        