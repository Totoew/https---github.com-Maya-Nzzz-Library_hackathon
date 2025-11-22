FROM python:3.12-slim

WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код
COPY . .

# Открываем порт
EXPOSE 5000

# Запуск Flask с автообновлением
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]
