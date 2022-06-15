from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from schema import OrderInSchema, ProductInSchema, FirmInSchema, StockInSchema, StockOutInSchema


class Demand(SQLModel, table=True):
    __tablename__ = "demands"
    batch_no: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    orders: List["Order"] = Relationship(back_populates="demand", sa_relationship_kwargs={
        "cascade": "all, delete"})  # one demand have many orders
    stockIn: List["StockIn"] = Relationship(back_populates="demand")


class Product(ProductInSchema, table=True):
    __tablename__ = "products"
    order: "Order" = Relationship(back_populates="product")
    stockIn: "StockIn" = Relationship(back_populates="product")
    stockOut: "StockOut" = Relationship(back_populates="product")


class Order(OrderInSchema, table=True):
    __tablename__ = "orders"
    Sr_no: Optional[int] = Field(default=None, primary_key=True)
    demand: Optional[Demand] = Relationship(back_populates="orders")
    product: Product = Relationship(back_populates="order")
    company: "Company" = Relationship(back_populates="order")


class Company(FirmInSchema, table=True):
    __tablename__ = "company"
    firm_id: Optional[int] = Field(default=None, primary_key=True)
    order: Order = Relationship(back_populates="company")


class StockIn(StockInSchema, table=True):
    __tablename__ = "stock_in"
    stock_in_id: Optional[int] = Field(primary_key=True, default=None)
    date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    product: Product = Relationship(back_populates="stockIn")
    demand: List[Demand] = Relationship(back_populates="stockIn",sa_relationship_kwargs={
        "cascade": "all, delete"})


class StockOut(StockOutInSchema, table=True):
    __tablename__ = "stock_out"
    stock_out_id: Optional[int] = Field(primary_key=True, default=None)
    date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    product: List[Product] = Relationship(back_populates="stockOut")
