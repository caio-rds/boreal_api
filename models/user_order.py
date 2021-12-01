from pydantic import BaseModel


class UserOrder(BaseModel):
    user: str
    order: float
    previousorder: bool
