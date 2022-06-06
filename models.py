from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class Demand(SQLModel, table=True):
    __tablename__ = "demands"
    batch_no: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    orders: List["Order"] = Relationship(back_populates="demand")

class Company(SQLModel, table=True):
    __tablename__ = "company"
    firm_id: Optional[int] = Field(default=None, primary_key=True)
    firm_name: str
    firm_address: str
    batch_no: int = Field(default_factory=None, foreign_key="demands.batch_no")



class Product(SQLModel, table=True):
    __tablename__ = "products"
    id: Optional[int] = Field(default=None, primary_key=True)
    barcode: str
    product_name: str
    product_description: str
    total_stock: int
    order: "Order" = Relationship(back_populates="product")
    stockin: "StockIn" = Relationship(back_populates="product")
    stockout: "StockOut" = Relationship(back_populates="product")


class Order(SQLModel, table=True):
    __tablename__ = "orders"
    Sr_no: Optional[int] = Field(default=None, primary_key=True)
    estimate_cost: int
    last_quantity_purchased: int
    date_of_last_purchased: Optional[str]
    stock_in_balance: int
    further_forecasted_requirement: int
    approved_rate: int
    unit_price: int
    packing: int
    total_amount_pk: str
    batch_no: int = Field(foreign_key="demands.batch_no")
    product_id: int = Field(foreign_key="products.id")
    product: Product = Relationship(back_populates="order")


class Stock(SQLModel):
    product_id: int = Field(foreign_key="products.id")
    date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    particulars: str


class StockIn(Stock, table=True):
    __tablename__ = "stock_in"
    stock_in_id: Optional[int] = Field(primary_key=True, default=None)
    received_quantity: int
    rate: float
    amount: float
    condemned_written_off: str
    product: Product = Relationship(back_populates="stockin")


class StockOut(Stock, table=True):
    stock_out_id: Optional[int] = Field(primary_key=True, default=None)
    bill_no: int
    issued_quantity: int
    product: Product = Relationship(back_populates="stockout")
