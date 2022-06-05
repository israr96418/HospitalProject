from fastapi import HTTPException, status, APIRouter
from models import StockIn, Product
from database import engine
from sqlmodel import Session, select, and_

session = Session(bind=engine)

router = APIRouter(
    prefix="/stock",
    tags=["Stock_in"]
)


@router.get('/get')
def index():
    statement = select(StockIn)
    stock_in_data = session.exec(statement).all()
    return stock_in_data


@router.post('/stockin', response_model=StockIn, status_code=status.HTTP_201_CREATED)
def Stock_IN(data: StockIn):
    stockin_post = StockIn(**data.dict())
    # if session.exec(
    #         select(Product).where(and_(Product.id == data.stock_in_id, Product.total_stock == data.received_quantity))):
    session.add(stockin_post)
    session.commit()
    session.refresh(stockin_post)
    return stockin_post
    # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Quantity does not match")
