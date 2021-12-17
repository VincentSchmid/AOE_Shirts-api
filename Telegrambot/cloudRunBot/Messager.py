from events.events import Events
from telegram.bot import Bot
from telegram import ParseMode
from Model import AppModel


class Messager():
    def __init__(self, model: AppModel) -> None:
        self.model: AppModel = model
        self.events: Events = model.events
        self.bot: Bot = model.bot
        
        self.model.events.send_message += self.send_telegram_message

    def send_telegram_message(self):
        self.bot.send_message(chat_id = self.model.chat_id,
                              text = self.model.message,
                              parse_mode=ParseMode.MARKDOWN_V2)

    def send_file(self):
        self.bot.send_document(chat_id = self.model.chat_id,
                          document = self.model.result)
                          