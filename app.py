from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("house_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])

    # Predict price
    price = model.predict([[area, bedrooms, bathrooms]])

    return render_template("index.html",
        prediction_text=f"Predicted Price: ₹ {round(price[0], 2)}")

if __name__ == "__main__":
    app.run(debug=True)
