# homework_04/models.py
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, exc
from sqlalchemy.exc import SQLAlchemyError

# Database URL (use environment variable or default)
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite+aiosqlite:///./test.db")  # SQLite для простоты

# Асинхронный алхимичный engine
engine = create_async_engine(DATABASE_URL, echo=False)  # echo=True для отладки SQL-запросов

# Declarative base
Base = declarative_base()

# Асинхронный Session object
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', username='{self.username}', email='{self.email}')"

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)

    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"Post(id={self.id}, user_id={self.user_id}, title='{self.title}')"

async def create_tables():
    """Создает таблицы в базе данных."""
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Таблицы успешно созданы.")
    except SQLAlchemyError as e:
        print(f"Ошибка при создании таблиц: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка при создании таблиц: {e}")
