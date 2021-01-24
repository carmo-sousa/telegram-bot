"""
All commands of Bot

TODO: Remover funções desnecessárias!
"""

import logging

from telegram import Update, ParseMode
from telegram.ext import CallbackContext

# Enable logging
logger = logging.getLogger(__name__)

# TODO: Terminar de escrever a pagina de ajuda.
HELP_MESSAGE = """
*Comandos*:
`/help` Mostra está pagina de ajuda.
`/new`  Salva um novo.
"""


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        "Olá, meu nome é Matatron\!\n"
        "Sou responsável por gerenciar seus dados\n"
        "Para saber mais digite `/help`",
        parse_mode=ParseMode.MARKDOWN_V2,
    )


def list(update: Update, context: CallbackContext):
    return


def add(update: Update, context: CallbackContext):
    pass


def edit(update: Update, context: CallbackContext):
    pass


def update(update: Update, context: CallbackContext):
    pass


def delete(update: Update, context: CallbackContext):
    pass


def cancel(update: Update, context: CallbackContext):
    pass


def help(update: Update, context: CallbackContext):
    user = update.message.from_user
    chat_id = update.effective_chat.id

    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(HELP_MESSAGE, parse_mode=ParseMode.MARKDOWN)
    pass


# TODO: Remover método!
# def echo(update: Update, context: CallbackContext):
#     chat_id = update.effective_chat.id
#     message_id = update.message.message_id

#     user = update.message.from_user
#     text = update.message.text

#     logging.info("Gender of %s: %s", user.first_name, text)

#     if text.lower() == "teste":
#         context.bot.kick_chat_member(user_id=user.id, chat_id=chat_id)
#         context.bot.delete_message(chat_id, message_id)

#     # update.message.reply_text(text)


def new(update: Update, context: CallbackContext):
    text = ""
    pass
