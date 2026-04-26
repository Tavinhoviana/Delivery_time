from src.main.composer.hubs_composer import compose_hubs_repository

repo = compose_hubs_repository()

def create_hub_controller(data):
    if "name" not in data or "city" not in data:
        return {"error": "missing fields"}, 400

    repo.insert_hub(
        name=data["name"],
        city=data["city"]
    )

    return {"message": "Hub created successfully"}, 201


def get_hub_by_name_controller(name):
    hub = repo.find_hub_by_name(name)

    if not hub:
        return {"error": "Hub not found"}, 404

    return {
        "id": hub[0],
        "name": hub[1],
        "city": hub[2]
    }, 200
