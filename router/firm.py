from typing import List

from fastapi import APIRouter, status
from sqlmodel import Session, select
from database import engine
from models import Company
from schema import Demand_IntSchema

session = Session(bind=engine)
router = APIRouter(
    prefix="/company",
    tags=["Company_Details"]
)


@router.get("/get", response_model=List[Company], status_code=status.HTTP_200_OK)
def get():
    query = session.exec(select(Company)).all()
    return query


@router.post("/post", status_code=status.HTTP_201_CREATED, response_model=Company)
def demand_generate(data: Company):
    company_details = Company(**data.dict())
    session.add(company_details)
    session.commit()
    session.refresh(company_details)
    return company_details
