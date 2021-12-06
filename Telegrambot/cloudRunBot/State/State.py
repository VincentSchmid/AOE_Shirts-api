from abc import ABC, abstractmethod
from Model import AppModel


class State(ABC):
    def __init__(self, appModel: AppModel):
        self.model = appModel

    @abstractmethod
    def document_received(self, document):
        pass

    @abstractmethod
    def stateInit(self):
        pass

    @abstractmethod
    def done_handler(self):
        pass

    @abstractmethod
    def start_handler(self):
        pass

    def send_message(self, text):
        self.model.message = text
        self.model.events.send_message()
