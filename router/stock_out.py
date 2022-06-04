
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from models import StockOut,Stock
from database import engine
from sqlmodel import Session, select

session = Session(bind=engine)

router = APIRouter(
     prefix="/stock",
    tags=["Stock"]
)

@router.get('/')
def index():
    return  {"StockOut : " : "Welcome to stockOut!"}


@router.post('/out' , response_model=StockOut, status_code=status.HTTP_201_CREATED)

def Stock_OUT(data : StockOut):
    stockout_post = StockOut(**data.dict())
    session.add(stockout_post)
    session.commit()
    session.refresh(stockout_post);
    
    return stockout_post 