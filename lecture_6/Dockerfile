FROM python:3.13-slim

# Установим системные зависимости (если нужны для сборки пакетов)
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Скопируем pyproject.toml (чтобы он был внутри контейнера, например для документации)
COPY pyproject.toml .

# Установим необходимые зависимости напрямую через pip
RUN pip install fastapi sqlalchemy uvicorn

# Скопируем остальной код
COPY . .

# Откроем порт
EXPOSE 8000

# Запуск приложения
CMD ["uvicorn", "book_api.main:app", "--host", "0.0.0.0", "--port", "8000"]



