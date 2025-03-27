 Домашнее задание 4: Асинхронная работа с сетью и БД

## Описание

Данный проект представляет собой решение четвертого домашнего задания по курсу "Base Python" от Otus.  Он демонстрирует асинхронную работу с сетью и базой данных, используя библиотеки `aiohttp` и `SQLAlchemy`.

Проект выполняет следующие задачи:

*   Получает данные о пользователях и постах с удаленного API (JSONPlaceholder).
*   Сохраняет полученные данные в базу данных SQLite (или PostgreSQL).
*   Использует асинхронные функции для повышения производительности.

## Технологии

*   Python 3.9+
*   aiohttp
*   SQLAlchemy (>=1.4)
*   aiosqlite (для SQLite)
*   asyncpg (для PostgreSQL)
*   asyncio

*   **`requirements.txt`:** Содержит список всех необходимых зависимостей Python.
*   **`homework_04/main.py`:**  Главный файл, который запускает асинхронное приложение.
*   **`homework_04/jsonplaceholder_requests.py`:** Отвечает за асинхронное получение данных из JSONPlaceholder API с использованием `aiohttp`.
*   **`homework_04/models.py`:** Определяет модели базы данных (User и Post) и содержит функции для работы с базой данных, используя `SQLAlchemy`.

## Установка и запуск

1.  **Клонируйте репозиторий (или скопируйте файлы):**

    ```bash
    git clone <your_repository_url>
    cd <your_project_directory>
    ```

2.  **Создайте виртуальное окружение (рекомендуется):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3.  **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Запустите приложение:**

    ```bash
    python homework_04/main.py
    ```

## Настройка базы данных

По умолчанию проект использует базу данных SQLite (`test.db`) в текущей директории.

