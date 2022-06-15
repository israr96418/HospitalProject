from typing import List

from fastapi import APIRouter, status, HTTPException
from sqlmodel import Session, select
from database import engine
from models import Product
from schema import ProductInSchema, ProductUpdateSchema

session = Session(bind=engine)
router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


# get all product
@router.get("/", response_model=List[Product], status_code=status.HTTP_200_OK)
def get_product():
    query = session.exec(select(Product)).all()
    return query


# create product
@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(data: ProductInSchema):
    product = Product(**data.dict())
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


# update product
@router.put("/{barcode}", status_code=status.HTTP_200_OK)
def update_product(data: ProductUpdateSchema, barcode: str):
    result = session.exec(select(Product).where(Product.barcode == barcode)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with barcode no {barcode} are not found")
    else:
        result.product_name = data.product_name
        result.product_description = data.product_description
        result.total_stock = data.total_stock
        session.commit()
        session.refresh(result)
        return result


# delete product
@router.delete("/{barcode}")
def delete_order(barcode: str):
    result = session.exec(select(Product).where(Product.barcode == barcode)).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with barcode no {barcode} are not found")
    else:
        session.delete(result)
        session.commit()
        return result
