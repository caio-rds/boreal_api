import requests
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from views import login, order, register
from models.user_order import UserOrder


app = FastAPI()

app.include_router(login.router)
app.include_router(order.router)
app.include_router(register.router)


