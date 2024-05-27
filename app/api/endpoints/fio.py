from fastapi import APIRouter
from app.utils import SystemException
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/fio")
def get_fio():
    try:
        return JSONResponse({"message": "Кисин Максим Олегович УБСТ2101"})
    except Exception as error:
        raise SystemException(error)

