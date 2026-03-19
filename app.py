from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load models
model = joblib.load("model/placement_model.pkl")
scaler = joblib.load("model/placement_model_scaler.pkl")
encoders = joblib.load("model/placement_model_enc.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        data = {
            "Student_ID": int(request.form["Student_ID"]),
            "Age": int(request.form["Age"]),
            "Gender": request.form["Gender"],
            "Degree": request.form["Degree"],
            "Branch": request.form["Branch"],
            "CGPA": float(request.form["CGPA"]),
            "Internships": int(request.form["Internships"]),
            "Projects": int(request.form["Projects"]),
            "Coding_Skills": int(request.form["Coding_Skills"]),
            "Communication_Skills": int(request.form["Communication_Skills"]),
            "Aptitude_Test_Score": int(request.form["Aptitude_Test_Score"]),
            "Soft_Skills_Rating": int(request.form["Soft_Skills_Rating"]),
            "Certifications": int(request.form["Certifications"]),
            "Backlogs": int(request.form["Backlogs"])
        }

        input_df = pd.DataFrame([data])

        # Encode categorical
        for col in ['Gender', 'Degree', 'Branch']:
            input_df[col] = encoders[col].transform(input_df[col])

        # Scale
        input_scaled = scaler.transform(input_df)

        # Predict
        prediction = model.predict(input_scaled)

        result = "Placed ✅" if prediction[0] == 1 else "Not Placed ❌"

        return render_template("result.html", result=result)

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)