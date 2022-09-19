import settings
import datetime
import fastapi.exceptions
import asyncio
import os
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from sqlalchemy.exc import IntegrityError,OperationalError
import Service
import importlib
from typing import Any
from fastapi import FastAPI, Request
from redis.exceptions import ConnectionError

from component.cache import cache
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession
from common.CommonError import Common500OutShema,Common500Status,TokenException
from common.globalFunctions import getorgeneratetoken, get_token

from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response
if os.name!='nt':
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
else:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from elasticsearchclient import es


app = FastAPI(redoc_url=None,docs_url=None,openapi_url=None)
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"],)

@app.middleware("http")
async def validate_tokenandperformevent(request: Request, call_next:Any)->Response:
    #todo: need verify the token expire date.and add refresh token.
    request.state.token=await getorgeneratetoken(request)
    print('token:',request.state.token)

    try:
        response = await call_next(request)  # This request will be modified and sent

    except OperationalError as e:
        jsonout = Common500OutShema(status=Common500Status.dberror,msg=str(e)).json()
        response=JSONResponse(jsonout,status_code=500)
        try:
            await request.state.db_client.close()
        except:
            pass
    except IntegrityError as e:
        jsonout = Common500OutShema(status=Common500Status.dberror, msg=str(e)).json()
        response=JSONResponse(jsonout,status_code=500)
        try:
            await request.state.db_client.close()
        except:
            pass
    except TokenException as e:
        jsonout = Common500OutShema(status=Common500Status.tokenerror, msg=str(e)).json()
        response=JSONResponse(jsonout,status_code=500)
    except fastapi.exceptions.ValidationError as e:
        jsonout = Common500OutShema(status=Common500Status.validateerror,msg='',data=e.errors()).json()
        response=JSONResponse(jsonout,status_code=500)
    except  ConnectionError as e:
        jsonout = Common500OutShema(status=Common500Status.cacheerror,msg='cache server error',data=str(e)).json()
        response=JSONResponse(jsonout,status_code=500)
    except Exception as e:
        #es
        doc = {
            'text': str(e),
            'request':str(request),
            'timestamp': datetime.datetime.now(),
        }
        await es.index(index=f"xtlog-{settings.MODE}", document=doc)
        if settings.DEBUG:
            raise

        jsonout = Common500OutShema(status=Common500Status.unknownerr, msg=str(e)).json()
        response=JSONResponse(jsonout,status_code=500)

    #if request.state.token.is_guest:
    #    response.set_cookie('token',Service.userService.create_access_token(request.state.token),expires=3600*24*30)
    return response

@app.on_event("startup")
async def startup()->None:
    if settings.MODE == 'DEV':
        from devtools import debugtools
        import multiprocessing
        backgroundprocess = multiprocessing.Process(target=debugtools.before_appstart)
        backgroundprocess.start()
    cache.init(prefix=settings.CACHE_PREFIX,expire=settings.DEFAULT_CACHE_EXPIRE,enable=settings.ENABLE_CACHE)


for f in Path(settings.BASE_DIR).joinpath('modules').rglob('*.py'):
    if f.name.endswith('Controller.py'):
        controller = importlib.import_module(
            str(f.relative_to(settings.BASE_DIR)).replace(os.sep,'.')[0:-3]
        )

        app.include_router(controller.router)




@app.get('/')
def forazureping()->dict:
    return {"status": 'success'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=80, log_level="info",reload=settings.DEBUG)