from telegram.files.file import File

from Model import AppModel
from State.State import State
from .State import Idle, RecievingShirts, ReturningResult, SettingBackground
from Messager import Messager
from Shirt_Processing import full_pipeline
from pathlib import Path


class Instance():
    def __init__(self, model) -> None:
        self.model: AppModel = model
        self.state: State = Idle(self.model)
        self.messager: Messager = Messager(self.model)

        self.model.events.started += self.on_started
        self.model.events.background_set += self.on_background_set
        self.model.evnets.shirts.shirts_received += self.on_shirts_received
        self.model.events.return_results += self.on_return_results
        

    def on_started(self):
        self.state = SettingBackground(self.model)

    def on_background_set(self):
        self.state = RecievingShirts(self.model)

    def on_shirts_received(self):
        self.state = ReturningResult(self.model)
    
    def on_return_results(self):
        for shirt in self.model.shirts:
            self.process_shirt(self.model.background.effective_attachment.get_file(), shirt.effective_attachment.get_file())

        self.model.events.started()

    def process_shirt(self, background: File, foreground: File):
        background_filename = Path(background.file_path).name
        foreground_filename = Path(foreground.file_path).name

        background_data = background.download_as_bytearray()
        foreground_data = foreground.download_as_bytearray()

        self.model.result = full_pipeline(background_filename, background_data, foreground_filename, foreground_data)
        self.messager.send_file()
