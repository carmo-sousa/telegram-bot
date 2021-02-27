import os
import logging

from dotenv import load_dotenv

# Carrega as váriaveis de ambiente do projeto.
load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


class Config:
    # Nível de permição do projeto.
    # https://developers.google.com/sheets/api/guides/authorizing
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    # ID da planilha
    SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
    RANGE_NAME = os.getenv("RANGE_NAME")

    # Token do bot do telegram
    # https://t.me/botfather
    TOKEN = os.getenv("TOKEN")
    PORT = os.getenv("PORT")
    pass