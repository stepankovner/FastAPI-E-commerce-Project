from fastapi import FastAPI
app = FastAPI()
messages_db = {0: "First post in FastAPI"}

@app.get("/messages")
async def read_messages() -> dict:
    pass

@app.get("/messages/{message_id}")
async def read_message(message_id: int) -> str:
    pass

@app.post("/messages")
async def create_message(message: str) -> str:
    pass

@app.put("/messages/{message_id}")
async def update_message(message_id: int, message: str) -> str:
    pass

@app.delete("/messages/{message_id}")
async def delete_message(message_id: int) -> str:
    pass

@app.delete("/messages")
async def delete_messages() -> str:
    pass
