from flask import Blueprint, jsonify, request
from src.main.composer.orders_composer import compose_orders_repository

orders_routes_bp = Blueprint("orders_routes", __name__)

repo = compose_orders_repository()

@orders_routes_bp.route("/orders", methods=["POST"])
def create_order():
    data = request.json

    repo.insert_order(
        hub_id=data["hub_id"],
        rider_id=data["rider_id"],
        created_at=data["created_at"],
        picked_up_at=data.get("picked_up_at"),
        delivered_at=data.get("delivered_at"),
        status=data["status"]
    )

    return jsonify({"message": "Order created"}), 201


@orders_routes_bp.route("/orders/analytics/hub", methods=["GET"])
def avg_delivery_time():
    result = repo.get_avg_delivery_time_per_hub()
    return jsonify(result)


@orders_routes_bp.route("/orders/analytics/slowest", methods=["GET"])
def slowest_hubs():
    result = repo.get_slowest_hubs()
    return jsonify(result)
