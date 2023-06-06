from fastapi import FastAPI

from src.controllers.agenda_controller import agenda_router
from src.controllers.associate_controller import associate_router

app = FastAPI()


@app.get("/health-check/")
async def pong():
    return {"message": "OK"}


app.include_router(associate_router, prefix="/associates"),
app.include_router(agenda_router, prefix="/agenda")
