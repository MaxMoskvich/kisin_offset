from fastapi import APIRouter
from app.api.endpoints import fio

api_router = APIRouter()

api_router.include_router(fio.router, prefix="/api/student", tags=["ФИО студента"])