from typing import Optional

from sqlmodel import SQLModel, Field


class Demand_IntSchema(SQLModel):
    Batch_no: int
