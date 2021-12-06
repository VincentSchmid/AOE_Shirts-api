from State import State
from telegram import Bot, Update
from telegram.ext import CallbackContext 


class Idle(State):
    def start_handler(self):
        self.model.events.started()
    