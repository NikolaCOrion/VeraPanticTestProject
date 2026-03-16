from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class ProfileCreate(BaseModel):
    name: str
    age: int

class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

profiles = [
    {"id":1, "name": "Vera", "age": 23},
    {"id":2, "name": "Mila", "age": 23},
    {"id":3, "name": "David", "age": 24}
]


@app.get("/my-first-endpoint/")
def my_first_endpoint():
    return {"hello": "world"}

@app.get("/profiles/")
def list_profiles():
    return profiles

@app.get("/profiles/{id}/")
def get_profile(id: int):
    for profile in profiles:
        if profiles["id"] == id:
            return profile
    return {"message": "Profile not found"}


@app.post("/profiles/")
def create_profile(payload: ProfileCreate):
    max_id = max(profile["id"] for profile in profiles)
    new_profile = {
        "id": max_id + 1,
        "name": payload.name,
        "age": payload.age
    }
    profiles.append(new_profile)
    return new_profile


@app.put("/profiles/{id}/")
def update_profile(id: int, payload: ProfileUpdate):
    for profile in profiles:
        if profile["id"] == id:
            if payload.name is not None:
                profile["name"] = payload.name
            if payload.age is not None:
                profile["age"] = payload.age
            return profile

    return {"message": "Profile not found"}


@app.delete("/profiles/{id}/")
def delete_profile(id: int):
    for profile in profiles:
        if profile["id"] == id:
            profiles.remove(profile)
            return {"message": "Profile deleted"}

    return {"message": "Profile not found"}