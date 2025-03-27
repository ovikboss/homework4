# homework_04/jsonplaceholder_requests.py
import asyncio
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_json(session: aiohttp.ClientSession, url: str) -> list[dict]:
    """Асинхронно получает JSON данные из указанного URL."""
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Вызывает исключение для кодов ошибок HTTP
            return await response.json()
    except aiohttp.ClientError as e:
        print(f"Ошибка при получении данных из {url}: {e}")
        return []
    except Exception as e:
        print(f"Непредвиденная ошибка при получении данных из {url}: {e}")
        return []

async def fetch_users_data(session: aiohttp.ClientSession) -> list[dict]:
    """Асинхронно получает данные о пользователях."""
    return await fetch_json(session, USERS_DATA_URL)

async def fetch_posts_data(session: aiohttp.ClientSession) -> list[dict]:
    """Асинхронно получает данные о постах."""
    return await fetch_json(session, POSTS_DATA_URL)