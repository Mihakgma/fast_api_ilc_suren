from fastapi import FastAPI
import uvicorn

from items_views import router as items_router

app = FastAPI()
app.include_router(items_router, prefix="/items-views")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
