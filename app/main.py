from fastapi import FastAPI

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
    ),
    User(
        organization="CallCenter",
        role=Role.WORKER
    )
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
