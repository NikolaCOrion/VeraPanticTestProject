from fastapi import FastAPI

app = FastAPI()


'''
create a new endpoint: /users/
and create a list of hardcoded user objects
each one should have properties:
id
name
age
'''


@app.get("/my-first-endpoint/")
def my_first_endpoint():
    return {"hello": "world"}
