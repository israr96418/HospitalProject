from fastapi import APIRouter, status, HTTPException
from sqlmodel import Session, select, join, and_
from database import engine
from models import Order, Product, Company, Demand
from schema import OrderInSchema

# product = Product()
# order = Order()

session = Session(bind=engine)
router = APIRouter(
    prefix="/order",
    tags=["Order"]
)


# get all order
@router.get("/", status_code=status.HTTP_200_OK)
def get_order():
    data = session.exec(
        select(Order, Product, Company, Demand).select_from(join(Order, Product)).where(
            and_(Order.barcode == Product.barcode, Order.company_id == Company.firm_id,
                 Order.batch_no == Demand.batch_no))).all()
    return data


# create order
@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(data: OrderInSchema):
    order_post = Order(**data.dict())
    session.add(order_post)
    session.commit()
    session.refresh(order_post)
    return order_post


# Update order
@router.put("/{ID}", status_code=status.HTTP_200_OK)
def update_demand(data: OrderInSchema, ID: int):
    result = session.exec(select(Order).where(Order.Sr_no == ID)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with Sr no {ID} is not found")
    else:
        result.estimate_cost = data.estimate_cost
        result.last_quantity_purchased = data.last_quantity_purchased
        result.date_of_last_purchased = data.date_of_last_purchased
        result.stock_in_balance = data.stock_in_balance
        result.further_forecasted_requirement = data.further_forecasted_requirement
        result.approved_rate = data.approved_rate
        result.unit_price = data.unit_price
        result.packing = data.packing
        result.total_amount_pk = data.total_amount_pk
        result.batch_no = data.batch_no
        result.barcode = data.barcode
        result.company_id = data.company_id
        session.commit()
        session.refresh(result)
        return result


# Delete order
@router.delete("/{ID}")
def delete_order(ID: int):
    result = session.exec(select(Order).where(Order.Sr_no == ID)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with Batch No {ID} is not found")
    else:
        session.delete(result)
        session.commit()
        return result
