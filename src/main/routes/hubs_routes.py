from flask import Blueprint, jsonify, request
from src.main.composer.hubs_composer import compose_hubs_repository

hubs_routes_bp = Blueprint("hubs_routes", __name__)

repo = compose_hubs_repository()

@hubs_routes_bp.route("/hubs", methods=["POST"])
def create_hub():
    data = request.json

    repo.insert_hub(
        name=data["name"],
        city=data["city"]
    )

    return jsonify({"message": "Hub created successfully"}), 201

@hubs_routes_bp.route("/hubs/<name>", methods=["GET"])
def get_hub_by_name(name):
    hub = repo.find_hub_by_name(name)

    if not hub:
        return jsonify({"error": "Hub not found"}), 404

    return jsonify({
        "id": hub[0],
        "name": hub[1],
        "city": hub[2]
    })
