from fastapi import HTTPException, status, APIRouter
from models import StockOut, Product
from schema import StockOutInSchema, StockOutUpdateSchema
from database import engine
from sqlmodel import Session, select

session = Session(bind=engine)

router = APIRouter(
    prefix="/stockOut",
    tags=["StockOut"]
)


# get all stock out
@router.get('/')
def get_stock_out():
    statement = select(StockOut, Product).join(Product).where(StockOut.barcode == Product.barcode)
    result = session.exec(statement).all()
    return result


# create stock
@router.post('/', response_model=StockOut, status_code=status.HTTP_201_CREATED)
def stock_out(data: StockOutInSchema):
    result = session.exec(select(Product)).all()
    for i in result:
        if i.barcode == data.barcode:
            if i.total_stock >= data.issued_quantity:
                print("True")
                i.total_stock -= data.issued_quantity
                add_data = StockOut(**data.dict())
                session.add(add_data)
                session.commit()
                session.refresh(add_data)
                return add_data
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"issued quantity is greater than present stock")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"barcode {data.barcode} are not found")


# update stock out
@router.put("/{ID}", status_code=status.HTTP_200_OK)
def update_stock_out(data: StockOutUpdateSchema, ID: int):
    result = session.exec(select(StockOut).where(StockOut.stock_out_id == ID)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock details with Id {ID} is not found")
    else:
        result.particulars = data.particulars
        result.bill_no = data.bill_no
        result.issued_quantity = data.issued_quantity
        session.commit()
        session.refresh(result)
        return result


# delete stock out
@router.delete("/{ID}")
def update_stock_out(ID: int):
    result = session.exec(select(StockOut).where(StockOut.stock_out_id == ID)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stock with id {ID} is not found")
    else:
        session.delete(result)
        session.commit()
        return result
