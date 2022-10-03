from enum import Enum

class UserRole(Enum):
    customer=0
    admin=1<<1
    proxylevel1=1<<2
    proxylevel2=1<<3
    makerteer=16

