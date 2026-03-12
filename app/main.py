from fastapi import FastAPI

app = FastAPI()

@app.get("/my-first-endpoint/")
def my_first_endpoint():
    return {"hello": "world"}