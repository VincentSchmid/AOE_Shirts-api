import os
import http

from flask import Flask, request
from werkzeug.wrappers import Response

from Model import AppModel
from Instance import Instance

from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, Filters, MessageHandler


app = Flask(__name__)

bot = Bot(token=os.environ["TOKEN"])
model = AppModel(bot, os.environ["SHIRT_POROCESSING_ADDRESS"])
instance = Instance(model)


dispatcher = Dispatcher(bot=bot, update_queue=None)

dispatcher.add_handler(CommandHandler("start", instance.on_start_command))
dispatcher.add_handler(CommandHandler("done", instance.on_done_command))
dispatcher.add_handler(CommandHandler("help", instance.on_help_command))

dispatcher.add_handler(MessageHandler(Filters.photo | Filters.document, 
                        instance.on_document_received))

@app.post("/")
def index() -> Response:
    dispatcher.process_update(
        Update.de_json(request.get_json(force=True), bot))

    return "", http.HTTPStatus.NO_CONTENT
