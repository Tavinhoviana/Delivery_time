from flask import Blueprint, jsonify, request
from src.main.composer.orders_composer import compose_orders_repository

orders_routes_bp = Blueprint("orders_routes", __name__)

repo = compose_orders_repository()

def validate_order(data):
    required = ["hub_id", "rider_id", "created_at", "status"]
    for field in required:
        if field not in data:
            raise ValueError(f"{field} is required")


@orders_routes_bp.route("/orders", methods=["POST"])
def create_order():
    try:
        data = request.json or {}
        validate_order(data)

        repo.insert_order(**data)

        return jsonify({"message": "Order created"}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@orders_routes_bp.route("/orders/analytics/hub", methods=["GET"])
def get_avg_delivery_time_per_hub():
    try:
        result = repo.get_avg_delivery_time_per_hub()

        return jsonify({
            "data": result
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Internal server error",
            "details": str(e)
        }), 500

@orders_routes_bp.route("/orders/analytics/slowest", methods=["GET"])
def slowest_hubs():
    result = repo.get_slowest_hubs()
    return jsonify(result)
