from typing import List

from fastapi import APIRouter, status, HTTPException
from sqlmodel import Session, select
from database import engine
from models import Company
from schema import FirmInSchema

session = Session(bind=engine)
router = APIRouter(
    prefix="/company",
    tags=["Company_Details"]
)


@router.get("/", response_model=List[Company], status_code=status.HTTP_200_OK)
def get():
    query = session.exec(select(Company)).all()
    return query


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Company)
def firm_details(data: FirmInSchema):
    details = Company(**data.dict())
    session.add(details)
    session.commit()
    session.refresh(details)
    return details


# update firm
@router.put("/{ID}", status_code=status.HTTP_200_OK)
def update_firm(data: FirmInSchema, ID: int):
    result = session.exec(select(Company).where(Company.firm_id == ID)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"company details with Id {ID} is not found")
    else:
        result.firm_name = data.firm_name
        result.firm_contact = data.firm_contact
        result.firm_address = data.firm_address
        session.commit()
        session.refresh(result)
        return result


# delete firm
@router.delete("/{ID}")
def delete_firm(ID: int):
    result = session.exec(select(Company).where(Company.firm_id == ID)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"company with id no {ID} is not found")
    else:
        session.delete(result)
        session.commit()
        return result
