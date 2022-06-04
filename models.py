from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Demand(SQLModel, table=True):
    Batch_no: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class Order(SQLModel, table=True):
    Sr_no: Optional[int] = Field(default=None, primary_key=True)
    estimate_cost: int
    last_quantity_purchased: int
    date_of_last_purchased: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    stock_in_balance: int
    further_forecasted_requirement: int
    approved_rate: int
    unit_price: int
    packing: int
    total_amount_pk: str
    batch_no: int = Field(foreign_key="demand.Batch_no")
    barcode: int = Field(foreign_key="product.barcode")


class Product(SQLModel, table=True):
    barcode: int = Field(primary_key=True)
    product_name: str
    product_description: str
    total_stock: int
#bhai uzair