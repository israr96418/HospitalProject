from fastapi import APIRouter
from sqlmodel import Session
from database import engine

session = Session(bind=engine)
router = APIRouter(
    prefix="/demand ",
    tags=["Demand"]
)


@router.get("/")
def get():
    return {"ksafskadjfk"}
