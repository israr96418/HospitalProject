from fastapi import FastAPI
from router import demand,order, product, stock_in, stock_out
app = FastAPI()


app.include_router(demand.router)
app.include_router(order.router)
app.include_router(product.router)
app.include_router(stock_in.router)
app.include_router(stock_out.router)