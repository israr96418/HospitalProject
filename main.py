from fastapi import FastAPI
from router import demand,order, product
app = FastAPI()


app.include_router(demand.router)
app.include_router(order.router)
app.include_router(product.router)