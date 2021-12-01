import requests
from fastapi import Depends, APIRouter
from models.user_order import UserOrder
from service.auth import AuthHandler


auth_handler = AuthHandler()

router = APIRouter()


@router.post('/order', status_code=200)
async def order(userorder: UserOrder, username=Depends(auth_handler.auth_wrapper)):
    response = []
    print(userorder)
    if username:
        response.append({
            'user': str(userorder.user),
            'order': float(userorder.order),
            'previousorder': bool(userorder.previousorder),
        })

    return response


# WORKING
@router.get('/beers')
async def get_bears(userorder: UserOrder, username=Depends(auth_handler.auth_wrapper)):
    url = requests.get('https://api.openbrewerydb.org/breweries')
    r = url.json()
    result = []
    for x in r:
        result.append({'name': x['name']})

    return result
