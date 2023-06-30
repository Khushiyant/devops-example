import pytest

def test_model_exists(model):
    assert model is not None

def test_model_predict(model):
    assert model.predict(2) == 4.5

def test_model_predict_type(model):
    assert type(model.predict(2)) == float

if __name__ == '__main__':
    pytest.main([__file__])