from .State import State


class ReturningResult(State):
    def stateInit(self):
        self.model.events.results.returned += self.done_handler
        self.model.events.return_results()
    
    def done_handler(self):
        self.send_message("done")
        