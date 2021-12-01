from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder

from controller.order import json_url_beer
from models.user_order import UserOrder
from service.auth import AuthHandler

auth_handler = AuthHandler()

router = APIRouter()


# will request a json body
@router.post('/order', status_code=200)
async def order(userorder: UserOrder, username=Depends(auth_handler.auth_wrapper)):
    if username:
        data = {
            'user': str(userorder.user),
            'order': float(userorder.order),
            'previousorder': bool(userorder.previousorder),
        }

    return jsonable_encoder(data)


# will return the name of beers
@router.get('/beers')
async def get_bears(username=Depends(auth_handler.auth_wrapper)):
    if username:
        r = json_url_beer()
        beer_name = []
        for x in r:
            beer_name.append(x['name'])

        return jsonable_encoder({"names": beer_name})
