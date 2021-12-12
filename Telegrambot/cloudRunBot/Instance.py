from telegram import Update
from telegram.bot import Bot
from telegram.files.file import File
from telegram.ext import CallbackContext

from Model import AppModel
from State.State import State
from State.Idle import Idle
from State.RecievingShirts import RecievingShirts
from State.ReturningResult import ReturningResult
from State.SettingBackground import SettingBackground
from State.Help import Help
from Messager import Messager
from Shirt_Processing import full_pipeline
from pathlib import Path


class Instance():
    def __init__(self, bot: Bot, url) -> None:
        self.bot = bot
        self.url = url
        self._state: State = None
        self._messager: Messager = None
        self.model: AppModel = None
        self.first_startup = True
        
    def on_start_command(self, update: Update, context: CallbackContext):
        self.get_model(update)

        if (self.first_startup):
            self._messager = Messager(self.model)
            self._state = Idle(self.model)

            self.model.events.started += self.on_started
            self.model.events.background_set += self.on_background_set
            self.model.events.shirts_received += self.on_shirts_received
            self.model.events.return_results += self.on_return_results
            self.first_startup = False

        self._state.start_handler()

    def on_help_command(self, update: Update, context: CallbackContext):
        self.get_model(update)

        self._state = Help(self.model)

    def on_done_command(self, update: Update, context: CallbackContext):
        self.get_model(update)

        self._state.done_handler()

    def on_document_received(self, update: Update, context: CallbackContext):
        self.get_model(update)

        self._state.document_received(update.message)

    def on_started(self):
        self._state = SettingBackground(self.model)

    def on_background_set(self):
        self._state = RecievingShirts(self.model)

    def on_shirts_received(self):
        self._state = ReturningResult(self.model)
    
    def on_return_results(self):
        for shirt in self.model.shirts:
            self.process_shirt(self.model.background.effective_attachment[-1].get_file(), shirt.effective_attachment[-1].get_file())
        self._state.done_handler()

    def process_shirt(self, background: File, foreground: File):
        background_filename = Path(background.file_path).name
        foreground_filename = Path(foreground.file_path).name

        background_data = background.download_as_bytearray()
        foreground_data = foreground.download_as_bytearray()

        self.model.result = full_pipeline(self.model.url, background_filename, background_data, foreground_filename, foreground_data)
        self._messager.send_file()

    def get_model(self, update: Update):
        self.model = AppModel.Init(update.message.chat_id, self.bot, self.url)
        self.model.update = update