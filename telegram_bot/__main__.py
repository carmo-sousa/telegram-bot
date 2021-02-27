import logging

from telegram import BotCommand, Update
from telegram.ext import Updater, CommandHandler
from telegram_bot.modules import help, start
from telegram_bot.modules import conv_handler
from telegram_bot.config import Config

logger = logging.getLogger(__name__)
config = Config()


# Todos os comandos do bot
commands = [
    BotCommand("start", "Inicia a conversa com o bot!"),
    BotCommand("help", "Mostra a pagina de ajuda."),
    BotCommand("new", "Adicionar novo usuário."),
    BotCommand("end", "Deletar usuário."),
]


def main():
    updater = Updater(config.TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(conv_handler)

    updater.bot.set_my_commands(commands)

    updater.start_webhook(
        listen="0.0.0.0",
        port=config.PORT,
        url_path=config.TOKEN
    )

    updater.bot.set_webhook("https://hidden-tundra-01728.herokuapp.com/" + config.TOKEN)

    # updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
