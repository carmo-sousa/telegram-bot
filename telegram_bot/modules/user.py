import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    Filters,
)
from telegram_bot.modules.utils import (
    valid_email,
    valid_password,
    valid_username,
)

logger = logging.getLogger(__name__)

EMAIL, USERNAME, PASSWORD, SAVE = map(chr, range(4))


def new(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)

    text = (
        "Vamos começar a adicionar um novo usuário!\n"
        "Agora envie seu e-mail.\n"
        "Para cancelar envie /cancel"
    )
    update.message.reply_text(text)
    return EMAIL


def email(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    input_message = update.message.text

    if valid_email(input_message):
        text = (
            "Entre com seu nome de usuário!\n"
            "Para pular essa etapa envie /skip."
        )
        context.user_data[EMAIL] = input_message
        update.message.reply_text(text)
        return USERNAME

    else:
        text = "Email invalído!\n" "Tente novamente ou envie /skip."
        update.message.reply_text(text)
        return EMAIL


def skip_email(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info(f"O usuário {user.first_name} não informou um email!")

    text = "Agora informe seu nome de usuário ou envie /skip."
    update.message.reply_text(text)
    return USERNAME


def username(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)

    input_text = update.message.text

    if valid_username(input_text):
        text = "Agora informe sua senha.\n" "A senha é obrigatória!"
        context.user_data[USERNAME] = input_text
        update.message.reply_text(text)
        return PASSWORD
    else:
        update.message.reply_text("Senha invalída!\n" "Tente novamente!")
        return USERNAME


def skip_username(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)

    text = "Agora informe sua senha.\n" "A senha é obrigatória!"
    update.message.reply_text(text)
    return PASSWORD


def password(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)

    keyboards = [
        [
            InlineKeyboardButton("Salvar", callback_data=str(SAVE)),
            InlineKeyboardButton("Cancelar", callback_data="cancel"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboards)

    input_text = update.message.text

    if valid_password(input_text):
        context.user_data[PASSWORD] = input_text
        data = context.user_data

        email = data.get(EMAIL, "-")
        username = data.get(USERNAME, "-")
        password = data.get(PASSWORD, "-")

        text = f"Dasdos do novo usuário:\nEmail: {email}\nUsuário: {username}\nSenha: {password}"

        update.message.reply_text(text, reply_markup=reply_markup)
        return SAVE

    else:
        update.message.reply_text("Senha invalída!\nTente novamente.")
        return PASSWORD


def save(update: Update, context: CallbackContext):
    logger.info("Os dados foram salvos!")

    update.callback_query.answer()
    update.callback_query.edit_message_text("O novo usuário foi salvo!")
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext):
    # user = update.message.from_user
    logger.info("O usuário não foi adicionado!")

    update.callback_query.edit_message_text("Você desistiu!")
    return ConversationHandler.END


def exit(update: Update, context: CallbackContext):
    logger.info("Cancelando a adição do usuário!")

    update.message.reply_text("Você desistiu de salvar o usuário!")

    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("new", new)],
    states={
        EMAIL: [
            MessageHandler(Filters.text & ~Filters.command, email),
            CommandHandler("skip", skip_email),
        ],
        USERNAME: [
            MessageHandler(Filters.text & ~Filters.command, username),
            CommandHandler("skip", skip_username),
        ],
        PASSWORD: [
            MessageHandler(Filters.text & ~Filters.command, password),
        ],
        SAVE: [
            CallbackQueryHandler(save, pattern=f"^{str(SAVE)}$"),
            CallbackQueryHandler(cancel, pattern=f"^cancel$"),
        ],
    },
    fallbacks=[CommandHandler("cancel", exit)],
)
