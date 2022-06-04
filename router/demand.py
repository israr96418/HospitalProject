from typing import List

from fastapi import APIRouter, status
from sqlmodel import Session, select
from database import engine
from models import Demand
from schema import Demand_IntSchema

session = Session(bind=engine)
router = APIRouter(
    prefix="/demand",
    tags=["Demand"]
)


@router.get("/get", response_model=List[Demand], status_code=status.HTTP_200_OK)
def get():
    query = session.exec(select(Demand)).all()
    return query


@router.post("/post", status_code=status.HTTP_201_CREATED, response_model=Demand)
def demand_generate(data: Demand_IntSchema):
    demand_data = Demand(**data.dict())
    session.add(demand_data)
    session.commit()
    session.refresh(demand_data)
    return demand_data
