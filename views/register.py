from fastapi import Depends, APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from service.auth import AuthHandler
from controller.register import RegisterController

auth_handler = AuthHandler()

router = APIRouter()


# if results retorn None, means that user already exists
@router.post('/register', status_code=200)
async def register(form_data: OAuth2PasswordRequestForm = Depends()):
    result = RegisterController().insert_user(form_data.username, form_data.password)
    if result is None:
        raise HTTPException(status_code=400, detail='Username already registred')
    return jsonable_encoder({'detail': f'User {form_data.username} Created'})


