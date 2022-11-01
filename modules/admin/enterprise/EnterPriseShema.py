#   timestamp: 2022-10-06T14:58:24+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
import settings


class BindEnterpriseInShema(BaseModel):
    user_id: str
    enterprise_name: str
