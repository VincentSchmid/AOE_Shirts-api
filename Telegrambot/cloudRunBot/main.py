import os
import http

from flask import Flask, request
from werkzeug.wrappers import Response

from Model import AppModel
from Instance import Instance
import options

from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, Filters, MessageHandler


TELEGRAM_TOKEN = os.environ["TOKEN"]
CONFIG_FILENAME = "config.yaml" if "CONFIG_FILE" not in os.environ else os.environ["CONFIG_FILE"]
SHIRT_PROCESSING_ADDRESS = os.environ["SHIRT_POROCESSING_ADDRESS"]

app = Flask(__name__)
bot = Bot(token=TELEGRAM_TOKEN)

app_options = options.get_options(CONFIG_FILENAME)
model = AppModel(bot, SHIRT_PROCESSING_ADDRESS)
instance = Instance(model, app_options)

dispatcher = Dispatcher(bot=bot, update_queue=None)

dispatcher.add_handler(CommandHandler(
    app_options["COMMANDS"]["START"], instance.on_start_command))
dispatcher.add_handler(CommandHandler(
    app_options["COMMANDS"]["DONE"], instance.on_done_command))
dispatcher.add_handler(CommandHandler(
    app_options["COMMANDS"]["HELP"], instance.on_help_command))

dispatcher.add_handler(MessageHandler(Filters.document,
                                      instance.on_document_received))

dispatcher.add_handler(MessageHandler(Filters.photo,
                                      instance.on_photo_received))


@app.post("/")
def index() -> Response:
    dispatcher.process_update(
        Update.de_json(request.get_json(force=True), bot))

    return "", http.HTTPStatus.NO_CONTENT
