from events import Events


class AppModel(object):
    def __init__(self):
        self.shirts = []
        self.background = None
        self.events = Events()
        self.message = ""
        self.update = None
        self.bot = None