from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import FastAPI
from service.auth import AuthHandler


auth_handler = AuthHandler()

router = APIRouter()

# @app.post('/login')
# def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = None
#     for x in users:
#         if x['username'] == form_data.username:
#             user = x
#             break
#
#     if (user is None) or (not auth_handler.verify_password(form_data.password, user['password'])):
#         raise HTTPException(status_code=401, detail='Invalid username and/or password')
#     token = auth_handler.encode_token(user['username'])
#     return {'acess_token': token}


@router.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {'name': username}


@router.get('/unprotected')
def unprotected():
    print('oi')
    return {"hello": "world"}
