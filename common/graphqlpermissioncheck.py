#type: ignore
from typing import List
def graphqlpermissioncheck(modelname,user_id:int,roles:List[int],merchant_id:int=0):
    if 1 in roles:
        return True #has root permission

