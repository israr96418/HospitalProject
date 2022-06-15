from typing import List

from fastapi import APIRouter, status, HTTPException
from sqlmodel import Session, select, join
from database import engine
from models import Demand, Product, StockIn, Order
from schema import DemandInSchema

session = Session(bind=engine)
router = APIRouter(
    prefix="/demand",
    tags=["Demand"]
)


# get all demand
@router.get("/", response_model=List[Demand], status_code=status.HTTP_200_OK)
def get_demand():
    query = session.exec(select(Demand)).all()
    return query


# create Demand
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Demand)
def generate_demand(data: DemandInSchema):
    demand_data = Demand(**data.dict())
    session.add(demand_data)
    session.commit()
    session.refresh(demand_data)
    return demand_data


# update demand
@router.put("/{ID}", status_code=status.HTTP_200_OK)
def update_demand(data: DemandInSchema, ID: int):
    result = session.exec(select(Demand).where(Demand.batch_no == ID)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Demand with Batch No {ID} is not found")
    else:
        result.batch_no = data.Batch_no
        session.commit()
        session.refresh(result)
        return result


# delete Demand
@router.delete("/{ID}")
def delete_demand(ID: int):
    result = session.exec(select(Demand).where(Demand.batch_no == ID)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Demand with Batch No {ID} is not found")
    else:
        session.delete(result)
        session.commit()
        return result
