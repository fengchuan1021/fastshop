import secrets

def getKey(length:int=16)->str:
    return secrets.token_hex(16)

