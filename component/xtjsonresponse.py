import typing
from starlette.responses import JSONResponse
import orjson
from common.globalFunctions import toBytesJson
class XTJsonResponse(JSONResponse):
    media_type = "application/json"
    def __init__(
        self,
        content: typing.Any,
        striplang:str='',
        **kwargs: typing.Any
    ) -> None:
        self.striplang = striplang
        super().__init__(content, **kwargs)
    def render(self, content: typing.Any) -> bytes:
        return toBytesJson(content,self.striplang)