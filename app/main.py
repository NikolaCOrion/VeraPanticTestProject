from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    age: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

'''
create a new endpoint: /users/
and create a list of hardcoded user objects
each one should have properties:
id
name
age

GET jednog usera po id
/users/{id}/

POST novog usera
/users/
payload
{
 "name": "test",
 "age": 25
}
(trebalo bi da od svih postojecih usera izvuce onog sa najvecim id i da mu dodeli za jedan veci broj za id)


PUT postojeceg usera
/users/{id}/

{
 "name": "updated",
 "age": 27
}

DELETE postojeceg usera
/users/{id}/


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

@app.get("/users/{id}/")
def get_user(id: int):
    for user in users:
        if user["id"] == id:
            return user
    return {"message": "User not found"}


@app.post("/users/")
def create_user(payload: UserCreate):
    max_id = max(user["id"] for user in users)
    new_user = {
        "id": max_id + 1,
        "name": payload.name,
        "age": payload.age
    }
    users.append(new_user)
    return new_user


@app.put("/users/{id}/")
def update_user(id: int, payload: UserUpdate):
    for user in users:
        if user["id"] == id:
            if payload.name is not None:
                user["name"] = payload.name
            if payload.age is not None:
                user["age"] = payload.age
            return user

    return {"message": "User not found"}


@app.delete("/users/{id}/")
def delete_user(id: int):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return {"message": "User deleted"}

    return {"message": "User not found"}