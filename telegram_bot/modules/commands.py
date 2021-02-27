"""
All commands of Bot
"""

import logging

from telegram import Update
from telegram.ext import CallbackContext

# Enable logging
logger = logging.getLogger(__name__)

# TODO: Terminar de escrever a pagina de ajuda.
HELP_MESSAGE = """
Bem vindo ao seu gerenciador de usuário e senha!

*Comandos*:
/help   Mostra está pagina de ajuda.
/new    Salva um novo.
/end    Finaliza a conversa.
"""


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    text = (
        f"Seu ID: {user.id}\n"
        "Bem vindo ao seu gerenciador de usuários pessoal!\n"
        "Para adicionar um novo usuário e senha digite /new.\n"
        "Para mais informações digite /help"
    )
    logger.info("Gender of %s: %s", user.first_name, update.message.text)

    update.message.reply_text(text=text)


def help(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(HELP_MESSAGE)


def job_callback(context: CallbackContext):
    job = context.job
    context.bot.send_message("325105532", job.context)
