import asyncio
import aiohttp
from typing import List
import jsonplaceholder_requests, models
from sqlalchemy import exc

async def create_users(users_data:List[dict]):
    """Создает записи пользователей в базе данных."""
    async with models.async_session() as session:
        try:
            users = [models.User(
                id=user_data['id'],
                name=user_data['name'],
                username=user_data['username'],
                email=user_data['email']
            ) for user_data in users_data]
            session.add_all(users)
            await session.commit()
            print(f"Успешно добавлено {len(users)} пользователей.")

        except exc.SQLAlchemyError as e:
            print(f"Ошибка при создании пользователей: {e}")
            await session.rollback() # rollback the session to a clean state

async def create_posts(posts_data:List[dict]):
    """Создает записи постов в базе данных."""
    async with models.async_session() as session:
        try:
            posts = [models.Post(
                id=post_data['id'],
                user_id=post_data['userId'],
                title=post_data['title'],
                body=post_data['body']
            ) for post_data in posts_data]
            session.add_all(posts)
            await session.commit()
            print(f"Успешно добавлено {len(posts)} постов.")

        except exc.SQLAlchemyError as e:
            print(f"Ошибка при создании постов: {e}")
            await session.rollback() # rollback the session to a clean state

async def async_main():
    """Асинхронная главная функция."""
    try:
        await models.create_tables() # Create tables
        async with aiohttp.ClientSession() as session:
            results = await asyncio.gather(
                jsonplaceholder_requests.fetch_users_data(session),
                jsonplaceholder_requests.fetch_posts_data(session),
                return_exceptions=True,  # Важно!  Чтобы asyncio.gather не выкидывал исключение
            )

        users_data, posts_data = results  # Извлекаем результаты

        if isinstance(users_data, Exception):
            print(f"Ошибка при получении данных о пользователях: {users_data}")
            users_data = [] # To prevent further errors
        if isinstance(posts_data, Exception):
            print(f"Ошибка при получении данных о постах: {posts_data}")
            posts_data = [] # To prevent further errors

        await create_users(users_data) # Create users
        await create_posts(posts_data)  # Create posts

        print("Данные успешно обработаны.")

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

def main():
    """Главная функция."""
    asyncio.run(async_main())

if __name__ == "__main__":
    main()