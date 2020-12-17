from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.user_router import router as router_users
from routers.transaction_router import router as router_transactions

api = FastAPI()

api.include_router(router_users)
api.include_router(router_transactions)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
    "https://cajero-app12.herokuapp.com"
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
