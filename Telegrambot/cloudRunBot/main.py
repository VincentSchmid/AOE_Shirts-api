import os
import http
from enum import Enum

from flask import Flask, request
from werkzeug.wrappers import Response

from telegram import Bot, Update, ForceReply
from telegram.ext import Dispatcher, CommandHandler, Filters, MessageHandler, CallbackContext

## LORD FORGIVE ME FOR THIS GOD AWFUL HACK JOB
app = Flask(__name__)

class State(Enum):
    IDLE = 0,
    SETTING_BACKGROUND = 1,
    RECIEVING_SHIRTS = 2,
    RETURNING_RESULT = 3

def start(update: Update, context: CallbackContext) -> None:
    global state
    state = State.SETTING_BACKGROUND
    
    bot.send_message(chat_id=update.message.chat_id, 
                    text="Send Background Image")


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)



shirts = []
background = ""
state = State.IDLE
bot = Bot(token=os.environ["TOKEN"])

dispatcher = Dispatcher(bot=bot, update_queue=None)

# on different commands - answer in Telegram
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))

# on non command i.e message - echo the message on Telegram
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))




def document_received(update: Update, context: CallbackContext) -> None:
    global state
    global background
    global shirts
    global bot
    if state == State.SETTING_BACKGROUND:
        background = update.message
        state == State.RECIEVING_SHIRTS
        bot.send_message(chat_id=update.message.chat_id,
                         text="Background Set")

        bot.send_message(chat_id=update.message.chat_id,
                         text="Send unedited shirt photos")

    if state == State.RECIEVING_SHIRTS:
        shirts.append(update.message)
        state == State.RETURNING_RESULT

    if state == State.RETURNING_RESULT:
        

dispatcher.add_handler(MessageHandler(Filters.video | Filters.photo | Filters.document, 
                         document_received))

@app.post("/")
def index() -> Response:
    dispatcher.process_update(
        Update.de_json(request.get_json(force=True), bot))

    return "", http.HTTPStatus.NO_CONTENT