from telegram.bot import Bot
from telegram.message import Message
from events import Events
from telegram.update import Update


class AppModel(object):
    def __init__(self, bot: Bot):
        self.bot: Bot = bot
        self.events: Events = Events()
        self.shirts = []
        self.background: Message = None
        self.result: bytes = None
        self.message: str = ""
        self.update: Update = None
    
    def clear_data(self):
        self.shirts = []
        self.background = None
        self.result = None
        self.message = ""
        self.update = None
        