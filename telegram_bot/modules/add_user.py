import logging

from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Filters,
)

logger = logging.getLogger(__name__)

NAME, CPF, DATA = range(3)


# TODO: Refazer a lógica de todas as funções!
def new(update: Update, context: CallbackContext):
    logger.info(update.message.text)
    update.message.reply_text("Vamos começar?\n\n1 - Sim\n2 - Não")
    return NAME


def name(update: Update, context: CallbackContext):
    logger.info(update.message.text)
    update.message.reply_text("Qual o nome do usuário?")
    return CPF


def cpf(update: Update, context: CallbackContext):
    logger.info(update.message.text)
    update.message.reply_text("Qual o CPF do novo colaborador?")
    return DATA


def data(update: Update, context: CallbackContext):
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext):
    logger.info(update.message.text)
    update.message.reply_text("Desistiu!")
    return ConversationHandler.END


conversation_handler = ConversationHandler(
    entry_points=[CommandHandler("new", new)],
    states={
        DATA: [
            MessageHandler(Filters.text("1") & ~Filters.command, data),
            MessageHandler(Filters.text("2") & ~Filters.command, cancel),
        ]
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
