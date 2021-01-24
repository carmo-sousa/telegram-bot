from __future__ import print_function
import pickle
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from telegram_bot.config import Config

from pprint import pprint

from telegram_bot.config import Config

config = Config()

# The ID and range of a sample spreadsheet.

SAMPLE_SPREADSHEET_ID = config.SAMPLE_SPREADSHEET_ID
SAMPLE_RANGE_NAME = config.SAMPLE_RANGE_NAME


config = Config()

# If modifying these scopes, delete the file token.pickle.
SCOPES = config.SCOPES


def service():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("sheets", "v4", credentials=creds)

    return service


def main(service):
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
        print("No data found.")
    else:
        print("Name, Major:")
        for row in values:
            # Print columns A and B, which correspond to indices 0 and 4.
            if len(row) < 3:
                break

            print("%s: \t[%s] %s" % (row[0], row[1], row[2]))
            # print(row)


def add_user(service):
    values = [["7 BPE", "01234567891"]]
    body = {"values": values}
    result = (
        service.spreadsheets()
        .values()
        .append(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range="Colaboradores!A:B",
            valueInputOption="RAW",
            body=body,
            # insertDataOption="INSERT_ROWS",
        )
        .execute()
    )

    updates = result.get("updates", 0)
    rows = updates.get("updatedRows")

    print(
        "{0} {1} adicionados.".format(
            rows, "Colaboradores" if rows > 1 else "Colaborador"
        )
    )
