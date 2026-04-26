from flask import Blueprint, jsonify, request
from src.main.composer.riders_composer import compose_riders_repository

riders_routes_bp = Blueprint("riders_routes", __name__)

repo = compose_riders_repository()

@riders_routes_bp.route("/riders", methods=["POST"])
def create_rider():
    data = request.json

    repo.insert_rider(
        name=data["name"],
        hub_id=data["hub_id"]
    )

    return jsonify({"message": "Rider created"}), 201

@riders_routes_bp.route("/riders", methods=["GET"])
def list_riders():
    riders = repo.get_all_riders()

    return jsonify(riders)
