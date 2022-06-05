from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from models import StockOut, Stock
from database import engine
from sqlmodel import Session, select

session = Session(bind=engine)

router = APIRouter(
    prefix="/stock",
    tags=["Stock_out"]
)


@router.get('/')
def index():
    statement = select(StockOut)
    stock_out_data = session.exec(statement).all()
    return stock_out_data


@router.post('/stockout', response_model=StockOut, status_code=status.HTTP_201_CREATED)
def Stock_OUT(data: StockOut):
    stockout_post = StockOut(**data.dict())
    session.add(stockout_post)
    session.commit()
    session.refresh(stockout_post)
    return stockout_post

