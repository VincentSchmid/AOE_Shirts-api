from events.events import Events
from telegram import Update
from telegram.ext import CallbackContext 
from Model import AppModel
from events import Events


class Messager():
    def __init__(self, model: AppModel) -> None:
        self.model = model
        self.events = model.events
        self.bot = model.bot
        self.model.events.send_message += self.send_telegram_message

    def send_telegram_message(self):
        self.bot.send_message(chat_id = self.model.update.message.chat_id,
                              text = self.model.message)
