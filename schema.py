from typing import Optional
from sqlmodel import SQLModel, Field


class DemandInSchema(SQLModel):
    Batch_no: int


class OrderInSchema(SQLModel):
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
    barcode: str = Field(foreign_key="products.barcode")
    company_id: int = Field(foreign_key="company.firm_id")


class ProductInSchema(SQLModel):
    barcode: str = Field(primary_key=True)
    product_name: str
    product_description: str
    total_stock: int
    price: float


class ProductUpdateSchema(SQLModel):
    product_name: str
    product_description: str
    total_stock: int
    price: float


class FirmInSchema(SQLModel):
    firm_name: str
    firm_contact: str
    firm_address: str


class StockInUpdateSchema(SQLModel):
    particulars: str
    received_quantity: int
    rate: float
    amount: float
    condemned_written_off: str
    batch_no: Optional[int] = Field(foreign_key="demands.batch_no")


class StockInSchema(StockInUpdateSchema):
    barcode: str = Field(foreign_key="products.barcode")


class StockOutUpdateSchema(SQLModel):
    bill_no: int
    particulars: str
    issued_quantity: int


class StockOutInSchema(StockOutUpdateSchema):
    barcode: str = Field(foreign_key="products.barcode")
