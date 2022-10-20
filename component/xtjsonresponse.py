import typing
from starlette.responses import JSONResponse
import orjson
from common.globalFunctions import toBytesJson
class XTJsonResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return toBytesJson(content)