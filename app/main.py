from fastapi import FastAPI

app = FastAPI()


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