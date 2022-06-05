from typing import List
import json
from fastapi import APIRouter, status
from sqlmodel import Session, select
from database import engine
from models import Demand, Order
from schema import Demand_IntSchema,Order_OutSchema

session = Session(bind=engine)
router = APIRouter(
    prefix="/order",
    tags=["Order"]
)


@router.get("/get", response_model=List[Order], status_code=status.HTTP_200_OK)
def get():
    statement = select(Order)
    orders = session.exec(statement).all()
    return orders


@router.post("/post", response_model=Order, status_code=status.HTTP_201_CREATED)
def post(data: Order):
    order_post = Order(**data.dict())
    session.add(order_post)
    session.commit()
    session.refresh(order_post)
    return order_post


# session.close()