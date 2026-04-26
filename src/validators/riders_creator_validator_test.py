from .riders_creator_validator import riders_creator_validator
class MockRequest:
    def __init__(self, body):
        self.body = body

def test_orders_creator_validator():
    request = MockRequest({
        "first_name": "guinga",
        "last_name": "cancun",
        "age": 3,
        "pet_id": 7
    })

    riders_creator_validator(request)