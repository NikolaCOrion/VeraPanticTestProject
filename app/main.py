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

users = [
    {"id":1, "name": "Vera", "age": 23},
    {"id":2, "name": "Mila", "age": 23},
    {"id":3, "name": "David", "age": 24}
]


@app.get("/my-first-endpoint/")
def my_first_endpoint():
    return {"hello": "world"}

@app.get("/users/")
def list_users():
    return users