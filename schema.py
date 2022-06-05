from datetime import datetime
from typing import Optional
from models import Demand

from sqlmodel import SQLModel, Field, Relationship


class Demand_IntSchema(SQLModel):
    Batch_no: int


class Order_OutSchema(SQLModel):
    # Sr_no: Optional[int] = Field(default=None, primary_key=True)
    estimate_cost: int
    last_quantity_purchased: int
    stock_in_balance: int
    further_forecasted_requirement: int
    approved_rate: int
    unit_price: int
    packing: int
    total_amount_pk: str
    # batch_no: int = Field(foreign_key="demand.Batch_no")
    # barcode: int = Field(foreign_key="product.barcode")
    # demand: Demand = Relationship(back_populates="order_list")
