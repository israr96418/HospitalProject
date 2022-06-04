
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from models import Stockin,Stock
from database import engine
from sqlmodel import Session, select

session = Session(bind=engine)

router = APIRouter(
     prefix="/stock",
    tags=["Stock"]
)

@router.get('/')
def index():
    return  {"Stock : " : "Welcome to stock!"}

@router.post('/newitems' , response_model= Stock)

def Stock_IN(data : Stockin):
    stockin_post = Stockin(**data.dict())
    session.add(stockin_post)
    session.commit()
    session.refresh(stockin_post)
    return stockin_post





