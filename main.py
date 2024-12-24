from typing import Annotated
from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items/{item_id}")
async def get_item_by_id(item_id: Annotated[int, Path(ge=0, le=1_000_000)]):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
