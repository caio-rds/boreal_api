from fastapi import FastAPI

from views import login, order, register

app = FastAPI()


app.include_router(login.router)
app.include_router(order.router)
app.include_router(register.router)


