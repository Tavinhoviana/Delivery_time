from .hubs_creator_validator import hubs_creator_validator

class MockRequest:
    def __init__(self, body):
        self.body = body

def test_person_creator_validator():
    request = MockRequest({
        "first_name": "guinga",
        "last_name": "cancun",
        "age": 3,
        "pet_id": 7
    })

    hubs_creator_validator(request)