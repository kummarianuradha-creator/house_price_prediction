import os
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

model_path = "model.pkl"

if os.path.exists(model_path):
    model = pickle.load(open(model_path, "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])

    price = model.predict([[area, bedrooms, bathrooms]])[0]

    return f"<h2>Estimated Price: ₹ {round(price,2)}</h2>"

if __name__ == "__main__":
    app.run()



