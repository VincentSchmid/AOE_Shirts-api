from telegram.bot import Bot
from telegram.message import Message
from events import Events
from telegram.update import Update


class AppModel(object):
    def __init__(self, bot: Bot):
        self.shirts = []
        self.background: Message = None
        self.result: bytes = None
        self.events: Events = Events()
        self.message: str = ""
        self.update: Update = None
        self.bot: Bot = bot
        