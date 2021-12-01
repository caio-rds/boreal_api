from fastapi import Depends, HTTPException, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from service.auth import AuthHandler
from controller.login import LoginController

auth_handler = AuthHandler()

router = APIRouter()


@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_exists = LoginController().user_exists(form_data.username)
    if user_exists:
        create_token = LoginController().autorize_login(form_data.username, form_data.password)
        return create_token
    else:
        raise HTTPException(status_code=401, detail='User does not exist')


@router.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return jsonable_encoder({'name': username})


@router.get('/unprotected')
def unprotected():
    return jsonable_encoder({'hello': 'world'})
