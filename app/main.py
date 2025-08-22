from fastapi import FastAPI
from app.db import create_tables

from app.models.user import Role, User

app = FastAPI()

admin = User(
    organization="CallCenter",
    role=Role.ADMIN
)

workers = [
    User(
        organization="CallCenter",
        role=Role.WORKER
    ),
    User(
        organization="CallCenter",
        role=Role.WORKER
    ),
    User(
        organization="CallCenter",
        role=Role.WORKER
    )
]

@app.on_event("startup")
def on_startup():
    create_tables()
@app.get("/")
async def root():
    return {"message": "Hello World"}
