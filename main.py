from fastapi import FastAPI
from router import demand, order, product, stock_in, stock_out,firm
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(demand.router)
app.include_router(order.router)
app.include_router(product.router)
app.include_router(stock_in.router)
app.include_router(stock_out.router)
app.include_router(firm.router)
