import os
import re
from typing import Tuple, Optional, Dict

from sqlalchemy.ext.asyncio import AsyncSession

import settings
import uuid
from azure.storage.blob import BlobServiceClient,BlobClient,PublicAccess
from azure.core.exceptions import ResourceNotFoundError
import Service
import datetime
from azure.storage.blob import ContentSettings
from pathlib import Path

from Service.payment import PayMethod


class PaypalService(PayMethod):
    async def getSession(self,db:AsyncSession,order_id:str) -> Dict:
        pass

    async def refund(self, db: AsyncSession,order_id:str,money:float) -> Dict:
        pass