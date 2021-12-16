from telegram.bot import Bot
from telegram.message import Message
from events import Events
from telegram.update import Update


class AppModel(object):
    def __init__(self, bot: Bot, processing_url):
        self.bot: Bot = bot
        self.events: Events = Events()
        self.shirts = []
        self.background = None
        self.result: bytes = None
        self.message: str = ""
        self._update: Update = None
        self.chat_id = None
        self.url = processing_url
        self.id = None
    
    def clear_data(self):
        self.shirts = []
        self.background = None
        self.result = None
        self.message = ""
        self._update = None

    @property
    def update(self) -> Update:
        return self._update
    
    @update.setter
    def update(self, update: Update):
        self._update = update
        self.chat_id = update.message.chat_id
