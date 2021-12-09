from State import State


class Idle(State):
    def start_handler(self):
        self.model.events.started()
        