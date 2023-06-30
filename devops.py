from flask import Flask
from flask import request
import pickle
 
class DummyModel:
    def __init__(self):
        pass
    def predict(self, data) -> float:
        return 2 * data + 0.5

# instance of flask application
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
 
# home route that returns below text when root url is accessed
@app.route("/predict")
def predict():
    request_data = request.args.get('data')
    return {
        "prediction": model.predict(float(request_data))
    }

 
if __name__ == '__main__': 
   app.run()