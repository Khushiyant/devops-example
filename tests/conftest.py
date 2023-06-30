import pytest

class DummyModel:
    def __init__(self):
        pass
    def predict(self, data) -> float:
        return 2 * data + 0.5

@pytest.fixture(scope="module")
def model():
    return DummyModel()