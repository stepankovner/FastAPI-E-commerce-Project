from fastapi import FastAPI, Request

from app.routers import categories, products, users, reviews

from starlette.middleware.sessions import SessionMiddleware

import time

# Создаём приложение FastAPI
app = FastAPI(
    title="FastAPI",
    version="0.1.0",
)
app.add_middleware(SessionMiddleware, secret_key="7UzGQS7woBazLUtVQJG39ywOP7J7lkPkB0UmDhMgBR8=")

# Подключаем маршруты категорий и товаров
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(users.router)
app.include_router(reviews.router)


# Корневой эндпоинт для проверки
@app.get("/")
async def root():
    """
    Корневой маршрут, подтверждающий, что API работает.
    """
    return {"message": "Добро пожаловать в API интернет-магазина!"}






