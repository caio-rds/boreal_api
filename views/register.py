from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database.database import Database
from service.auth import AuthHandler
from controller.register import RegisterController

auth_handler = AuthHandler()

router = APIRouter()


@router.post('/register', status_code=201)
async def register(form_data: OAuth2PasswordRequestForm = Depends()):
    result = RegisterController().insert_user(form_data.username, form_data.password)
    print(result)
    if result is None:
        raise HTTPException(status_code=400, detail='Username already registred')
    return result


