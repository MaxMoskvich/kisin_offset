from fastapi import FastAPI
from app.config import Config
from app.utils import SystemException
from app.api.router import api_router
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.middleware.gzip import GZipMiddleware

application = FastAPI(title=f"API FIO ({Config.DEPLOY_ENVIRONMENT})", version="0.1")

application.include_router(api_router, prefix="")

application.add_middleware(GZipMiddleware, minimum_size=500)

@application.exception_handler(SystemException)
async def system_exception_handler(request: Request, exception: SystemException):
    return JSONResponse(status_code=500, content={"error_message" : f"{exception.message}"})