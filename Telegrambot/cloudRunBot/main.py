import os
import http

from fastapi import Request, FastAPI
from werkzeug.wrappers import Response

from Model import AppModel
from Instance import Instance

from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, Filters, MessageHandler


app = FastAPI()

bot = Bot(token=os.environ["TOKEN"])
model = AppModel(bot)
instance = Instance(model)


dispatcher = Dispatcher(bot=bot, update_queue=None)

dispatcher.add_handler(CommandHandler("start", instance.on_start_command))
dispatcher.add_handler(CommandHandler("done", instance.on_done_command))

dispatcher.add_handler(MessageHandler(Filters.video | Filters.photo | Filters.document, 
                        instance.on_document_received))

@app.post("/")
def index(request: Request) -> Response:
    dispatcher.process_update(
        Update.de_json(request.json(), bot))

    return "", http.HTTPStatus.NO_CONTENT
