
from flask import Flask
import os
import pickle

app = Flask(__name__)

model = None
model_path = os.path.join(os.getcwd(), "house_model.pkl")

if os.path.exists(model_path):
    model = pickle.load(open(model_path, "rb"))
else:
    print("model file not found")

@app.route("/")
def home():
    return "House Price Website is running successfully ✅"

if __name__ == "__main__":
    app.run()

