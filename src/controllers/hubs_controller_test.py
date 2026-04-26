from src.controllers.hubs_controller import create_hub_controller

def test_create_hub_success(monkeypatch):
    class FakeRepo:
        def insert_hub(self, name, city):
            self.called = True

    fake_repo = FakeRepo()

    # substitui repo global
    monkeypatch.setattr(
        "src.controllers.hubs_controller.repo",
        fake_repo
    )

    response, status_code = create_hub_controller({
        "name": "Hub SP",
        "city": "São Paulo"
    })

    assert status_code == 201
    assert response["message"] == "Hub created successfully"
