## 🌐 Live Demo
- App: https://flask-lab1-starter.onrender.com/
- Healthcheck: https://flask-lab1-starter.onrender.com/healthcheck
# Flask Lab 1 — Starter

Базовий Flask-проєкт із ендпоінтами `/` (вітання) та `/healthcheck` і готовими `Dockerfile` та `docker-compose.yml`. Підходить для деплою на **Render.com**.

## Локальний запуск (без Docker)

```bash
python -m venv env
# Linux/macOS
source env/bin/activate
# Windows (PowerShell)
# .\env\Scripts\Activate.ps1

pip install -r requirements.txt
# Запуск (порт 8080 за замовчуванням)
export FLASK_APP=app && export FLASK_RUN_PORT=8080 && flask run -h 0.0.0.0
# Windows PowerShell:
# $env:FLASK_APP="app"; $env:FLASK_RUN_PORT="8080"; flask run -h 0.0.0.0
```

Перевірка:
- http://localhost:8080/ → `{ "message": "Hello, friend! ..." }`
- http://localhost:8080/healthcheck → `{ "status": "ok", "date": "..." }`

## Docker

```bash
# Збірка іміджу
docker build -t flask-lab1:latest .

# Запуск
docker run -it --rm -e PORT=8080 -p 8080:8080 flask-lab1:latest
```

## docker-compose

```bash
docker-compose build
docker-compose up
```

Далі перевіряйте ті самі URL:
- http://localhost:8080/
- http://localhost:8080/healthcheck

## Деплой на Render.com (через Dockerfile)

1. Завантажте код у GitHub-репозиторій.
2. У **Render** створіть **New → Web Service**.
3. Оберіть ваш репозиторій, дайте назву сервісу, регіон **(EU)**.
4. Тип деплою: **Docker** (Render сам знайде `Dockerfile`).
5. Ніяких команд запуску додавати не потрібно — використовується `CMD` із `Dockerfile`.
6. Після деплою відкрийте URL сервісу й перевірте ендпоінти.

### Поради для репозиторію

- Зробіть осмислені коміти:
  - `chore: scaffold Flask app`
  - `feat: add /healthcheck endpoint`
  - `chore: add Dockerfile and docker-compose`
  - `docs: add README with run instructions`
- Обов’язково додайте посилання на задеплоєний URL у README.

## Структура
```
flask-lab1-starter/
  app/
    __init__.py
    views.py
  .gitignore
  Dockerfile
  docker-compose.yml
  README.md
  requirements.txt
```

Успіхів!
## Author
Andrii Burlii, ІО-32
