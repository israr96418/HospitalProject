from fastapi import FastAPI
from router import demand
app = FastAPI()


app.include_router(demand.router)