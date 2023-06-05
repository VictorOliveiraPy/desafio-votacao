from fastapi import FastAPI

app = FastAPI()


@app.get("/health-check/")
async def pong():
    return {"message": "OK"}

