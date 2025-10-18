from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

async def check_auth(token: str):
    if token == "secret": return True
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

@app.get("/profile")
async def get_profile(is_authorized: bool = Depends(check_auth)):
    return "User is authorized"



# @app.get("/messages")
# async def all_messages(limit: int = 10, page: int = 1):
#     return {"messages": [{'limit': limit, 'page': page}]}


# @app.get("/comments")
# async def all_comments(limit: int = 10, page: int = 1):
#     return {"comments": [{'limit': limit, 'page': page}]}