from fastapi import FastAPI

from web import borrowings as bor

app = FastAPI()
app.include_router(bor.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', reload=True, port=8080)
