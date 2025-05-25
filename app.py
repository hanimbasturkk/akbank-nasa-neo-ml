from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open("models/neo_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            est_diameter_min = float(request.form["est_diameter_min"])
            est_diameter_max = float(request.form["est_diameter_max"])
            relative_velocity = float(request.form["relative_velocity"])
            miss_distance = float(request.form["miss_distance"])
            absolute_magnitude = float(request.form["absolute_magnitude"])

            features = np.array([[est_diameter_min, est_diameter_max, relative_velocity, miss_distance, absolute_magnitude]])
            
            pred = model.predict(features)[0]
            prediction = "Tehlikeli" if pred == 1 else "Tehlikesiz"

            # Tahmini sonucuyla sonuc.html sayfasını render et
            return render_template("sonuc.html", prediction=prediction)

        except Exception as e:
            error = f"Girdi veya model tahmininde hata: {e}"
            return render_template("index.html", error=error)
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
