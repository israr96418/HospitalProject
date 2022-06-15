from fastapi import HTTPException, status, APIRouter
from models import StockIn, Product, Demand
from database import engine
from sqlmodel import Session, select, join
from schema import StockInSchema, StockInUpdateSchema

session = Session(bind=engine)

router = APIRouter(
    prefix="/stockIn",
    tags=["StockIn"]
)


# get stock_in all data
@router.get('/')
def get_stock_in():
    statement = select(StockIn, Demand).select_from(join(StockIn, Demand)).where(
        StockIn.batch_no == Demand.batch_no)
    # statement = select(StockIn)
    stocking = session.exec(statement).all()
    return stocking


# create stock_in data
@router.post('/', response_model=StockIn, status_code=status.HTTP_201_CREATED)
def stock_in(data: StockInSchema):
    result = session.exec(select(Product)).all()
    for i in result:
        if i.barcode == data.barcode:
            print("True")
            i.total_stock += data.received_quantity
            add_data = StockIn(**data.dict())
            session.add(add_data)
            session.commit()
            session.refresh(add_data)
            return add_data
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"product with barcode {data.barcode} are not demanded")


# update stocking
@router.put("/{ID}", status_code=status.HTTP_200_OK)
def update_stock_in(data: StockInUpdateSchema, ID: int):
    result = session.exec(select(StockIn).where(StockIn.stock_in_id == ID)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock details with Id {ID} is not found")
    else:
        result.particulars = data.particulars
        result.received_quantity = data.received_quantity
        result.rate = data.rate
        result.amount = data.amount
        result.condemned_written_off = data.condemned_written_off
        result.batch_no = data.batch_no
        session.commit()
        session.refresh(result)
        return result


# delete stocking
@router.delete("/{ID}")
def delete_stock_in(ID: int):
    result = session.exec(select(StockIn).where(StockIn.stock_in_id == ID)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stock with id no {ID} is not found")
    else:
        session.delete(result)
        session.commit()
        return result
