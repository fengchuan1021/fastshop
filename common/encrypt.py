import secrets

def generateKey(length:int=16)->str:
    return secrets.token_hex(16)

