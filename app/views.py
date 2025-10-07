from flask import Blueprint, jsonify, request
from datetime import datetime, timezone

bp = Blueprint("views", __name__)

@bp.get("/")
def index():
    user = request.args.get("user", "friend")
    return jsonify(message=f"Hello, {user}! Welcome to Flask Lab 1 👋")

@bp.get("/healthcheck")
def healthcheck():
    # ISO 8601 UTC timestamp with Z suffix
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return jsonify(status="ok", date=now), 200
