import re
from datetime import datetime

def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").strip()
    return len(cpf) == 11 and cpf.isdigit()

def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) >= 8

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False
