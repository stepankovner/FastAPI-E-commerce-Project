from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel, Field, EmailStr, PositiveInt, NonNegativeInt, SecretStr
from typing import Optional
from decimal import Decimal
from datetime import datetime

app = FastAPI()

class Note(BaseModel):
    id: int
    text: str

notes = [
    Note(id=1, text="Купить хлеб"),
    Note(id=2, text="Написать отчет"),
    Note(id=3, text="Позвонить маме"),
    Note(id=4, text="Сходить в спортзал"),
    Note(id=5, text="Прочитать книгу")
]

@app.delete("/notes/{note_id}", response_model=Note)
async def delete_note(note_id: int) -> Note:
    for i, note in enumerate(notes):
        if note_id == note.id:
            notes.pop(i)
            return note
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")



























# class User(BaseModel):
#     username: str = Field(..., min_length=3, max_length=50, description="Имя пользователя")
#     email: EmailStr = Field(..., description="Электронная почта пользователя")
#     is_active: bool = Field(default=True, description="Статус активности пользователя")

# class Task(BaseModel):
#     title: str = Field(..., min_length=1, max_length=100, description="Название задачи")
#     description: Optional[str] = Field(default=None, max_length=500, description="Описание задачи")
#     is_completed: bool = Field(default=False, description="Статус завершения задачи")

# class Order(BaseModel):
#     order_id: PositiveInt = Field(..., description="Уникальный идентификатор заказа")
#     user_id: PositiveInt = Field(..., description="Идентификатор пользователя, сделавшего заказ")
#     total_amount: Decimal = Field(..., ge=0, description="Общая сумма заказа")
#     created_at: datetime = Field(..., description="Дата и время создания заказа")

# class Address(BaseModel):
#     user_id: PositiveInt = Field(..., description="Идентификатор пользователя")
#     city: str = Field(..., min_length=2, max_length=100, description="Город")
#     street: str = Field(..., min_length=2, max_length=200, description="Улица")
#     postal_code: int = Field(..., min_length=101000, max_length=999999, description="Почтовый индекс")

# class Product(BaseModel):
#     product_slug: str = Field(..., min_length=3, max_length=120, pattern=r"^[a-zA-Z0-9-_]*$", description="Слаг продукта")
#     name: str = Field(..., min_length=3, max_length=100, description="Название продукта")
#     price: Decimal = Field(..., gt=0, description="Цена продукта")
#     stock: NonNegativeInt = Field(default=0, description="Количество продукта на складе")

# class Post(BaseModel):
#     author_id: PositiveInt = Field(..., description="Идентификатор автора")
#     title: str = Field(..., max_length=100, description="Заголовок записи, не более 100 символов")
#     description: str | None = Field(default=None, max_length=250б description="Описание записи, не более 250 символов")
#     content: str = Field(..., description="Контент записи")
#     created_at: datetime = Field(default_factory=datetime.now, description="Запись создана")
#     updated_at: datetime | None = Field(default=None, description="Запись обновлена")
#     is_published: bool = Field(default=False, description="Запись опубликована")
#     tags: list[str] = Field(default=[], description="Теги записи")

# class User(BaseModel):
#     username: str = Field(..., min_length=5, max_length=20, description="Пользовательское имя, от 5 до 20 символов")
#     password: SecretStr = Field(..., min_length=8, max_length=50, description="Пароль, от 8 до 50 символов")
#     email: EmailStr = Field(..., description="Электронная почта")
#     first_name: str | None = Field(default=None, min_length=2, max_length=30, description="Имя, от 2 до 30 символов")
#     last_name: str | None = Field(default=None, min_length=2, max_length=30, description="Фамилия, от 2 до 30 символов")
#     is_active: bool = Field(default=True, description="Учётная запись активна")
#     is_staff: bool = Field(default=False, description="Является служебным пользователем")
#     is_superuser: bool = Field(default=False, description="Является суперпользователем")
#     date_joined: datetime = Field(default_factory=datetime.now, description="Зарегистрирован")
#     last_login: datetime | None = Field(default=None, description="Последнее посещение")












# class MessageCreate(BaseModel):
#     content: str

# class Message(BaseModel):
#     id: int
#     content: str

# messages_db: list[Message] = [Message(id=0, content="First post in FastAPI")]    

# @app.get("/messages", response_model=list[Message])
# async def read_messages() -> list[Message]:
#     return messages_db

# @app.get("/messages/{message_id}", response_model=Message)
# async def read_message(message_id: int) -> Message:
#     for message in messages_db:
#         if message.id == message_id:
#             return message
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

# @app.post("/messages", response_model=Message, status_code=status.HTTP_201_CREATED)
# async def create_message(message_create: MessageCreate) -> Message:
#     next_id = max((msg.id for msg in messages_db), default=-1) + 1
#     new_message = Message(id=next_id, content=message_create.content)
#     messages_db.append(new_message)
#     return new_message

# @app.put("/messages/{message_id}", response_model=Message)
# async def update_message(message_id: int, message_create: MessageCreate) -> Message:
#     for i, message in enumerate(messages_db):
#         if message.id == message_id:
#             updated_message = Message(id=message_id, content=message_create.content)
#             messages_db[i] = updated_message
#             return updated_message
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Сообщение не найдено")

# @app.delete("/messages/{message_id}", status_code=status.HTTP_200_OK)
# async def delete_message(message_id: int) -> dict:
#     for i, message in enumerate(messages_db):
#         if message.id == message_id:
#             messages_db.pop(i)
#             return {"detail": f"Message ID={message_id} deleted!"}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

# @app.delete("/messages", status_code=status.HTTP_200_OK)
# async def delete_messages() -> dict:
#     messages_db.clear()
#     return {"detail": "All messages deleted!"}











# comments_db = {0: "First comment in FastAPI"}

# @app.get("/comments")
# async def get_comments() -> dict:
#     return comments_db

# @app.get("/comments/{comment_id}")
# async def get_comment(comment_id: int) -> str:
#     if comment_id not in comments_db:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
#     return comments_db[comment_id]

# @app.post("/comments", status_code=status.HTTP_201_CREATED)
# async def post_comment(message: str = Body(...)) -> str:
#     current_index = max(comments_db) + 1 if comments_db else 0
#     comments_db[current_index] = message
#     return "Comment created!"

# @app.put("/comments/{comment_id}")
# async def put_comment(comment_id: int, message: str = Body(...)) -> str:
#     if comment_id not in comments_db:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
#     comments_db[comment_id] = message
#     return "Comment updated!"

# @app.delete("/comments/{comment_id}")
# async def delete_comment(comment_id: int) -> str:
#     if comment_id not in comments_db:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
#     comments_db.pop(comment_id)
#     return "Comment deleted!"

