import logging

from telegram.ext import Updater, CommandHandler
from telegram.botcommand import BotCommand
from telegram_bot.modules.commands import start, help
from telegram_bot.modules.add_user import conversation_handler
from telegram_bot.config import Config

logger = logging.getLogger(__name__)
config = Config()

# Todos os comandos do bot
commands = [
    BotCommand("start", "Inicia a conversa com o bot!"),
    BotCommand(
        "help", "Mostra a pagina de ajuda com a descrição dos comandos."
    ),
    BotCommand("new", "Adicionar novo usuário."),
    BotCommand("edit", "Editar usuário."),
    BotCommand("delete", "Deletar usuário."),
]


def main():
    updater = Updater(config.TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(conversation_handler)

    updater.bot.set_my_commands(commands)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()