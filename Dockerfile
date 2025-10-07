# Base image
FROM python:3.11.3-slim-bullseye

# Workdir inside container
WORKDIR /app

# Install deps early (better caching)
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Flask entrypoint config
ENV FLASK_APP=app

# Render.com provides PORT env; default to 8080 locally
ENV PORT=8080

# Start the app
CMD flask run -h 0.0.0.0 -p $PORT
