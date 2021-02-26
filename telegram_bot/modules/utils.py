import re


def show(data: dict):

    lista = []

    for key, value in data.items():
        lista.append(f"- {value}")

    return "\n".join(lista)


def valid_email(string):
    pattern = r"^[^-.][a-zA-Z0-9.-]+@[a-z]+\.[a-zA-Z]+[^-.]$"
    res = True if re.match(pattern, string) else False
    return res


def valid_password(string):
    pattern = r"^[a-zA-z0-9@.\-_]{8,32}$"
    res = True if re.match(pattern, string) else False
    return res


def valid_username(string):
    pattern = r"^[a-zA-z0-9@.\-_]{4,64}$"
    res = True if re.match(pattern, string) else False
    return res
