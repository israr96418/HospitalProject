from typing import List

from fastapi import APIRouter, status
from sqlmodel import Session, select
from database import engine
from models import Demand, Order
from schema import Demand_IntSchema

session = Session(bind=engine)
router = APIRouter(
    prefix="/order",
    tags=["Order"]
)


@router.get("/")
def get():
    return {"sjdkja"}


@router.post("/post", response_model=Order, status_code=status.HTTP_201_CREATED)
def post(data: Order):
    order_post = Order(**data.dict())
    session.add(Order)
    session.commit()
    session.refresh(order_post)
    return order_post
