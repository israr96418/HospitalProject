from typing import List

from fastapi import APIRouter, status
from sqlmodel import Session, select
from database import engine
from models import Demand, Order, Product
from schema import Demand_IntSchema

session = Session(bind=engine)
router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@router.get("/get", response_model=List[Product], status_code=status.HTTP_200_OK)
def get():
    query = session.exec(select(Product)).all()
    return query


@router.post("/post", response_model=Product, status_code=status.HTTP_201_CREATED)
def product_post(data: Product):
    product = Product(**data.dict())
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


