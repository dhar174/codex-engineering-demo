from fastapi import FastAPI, HTTPException

app = FastAPI(title="Codex Engineering Demo")

USERS = [
    {"id": 1, "name": "Ada Lovelace"},
    {"id": 2, "name": "Grace Hopper"},
    {"id": 3, "name": "Alan Turing"},
]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/users")
def list_users():
    return USERS


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in USERS:
        if user["id"] == user_id:
            return user

    raise HTTPException(status_code=404, detail="User not found")
