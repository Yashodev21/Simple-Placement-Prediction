# 🎯 Placement Predictor (ML Web App)

A Machine Learning-based web application that predicts whether a student will be placed or not based on academic performance, skills, and other factors.

---

## 🚀 Features

- 🔍 Predicts student placement (Placed / Not Placed)
- 🤖 Machine Learning model integration
- 🌐 Flask-based web application
- 🎨 Responsive and modern UI
- ⚡ Fast predictions using trained `.pkl` files

---

## 🧠 Tech Stack

- Frontend: HTML, CSS  
- Backend: Flask (Python)  
- ML Libraries: Scikit-learn, Pandas, NumPy  
- Model Handling: Joblib  

---

## 📁 Project Structure
- placement-predictor/
- │
- ├── app.py
- ├── requirements.txt
- │
- ├── model/
- │ ├── placement_model.pkl
- │ ├── placement_model_scaler.pkl
- │ └── placement_model_enc.pkl
- │
- ├── templates/
- │ ├── index.html
- │ └── result.html
- │
- └── static/
- └── style.css

---

## 🧾 Input Parameters

- Student_ID
- Age
- Gender (Male/Female)
- Degree (B.Tech, BCA, B.Sc, MCA)
- Branch (CSE, ECE, ME)
- CGPA
- Internships
- Projects
- Coding Skills
- Communication Skills
- Aptitude Test Score
- Soft Skills Rating
- Certifications
- Backlogs

---

## 📊 Output

- ✅ Placed  
- ❌ Not Placed  

---

## ⚠️ Important Notes

- Inputs must match training format  
- Categorical values are case-sensitive  
- Keep `.pkl` files inside `model/` folder  

---

## 🔮 Future Improvements

- Add placement probability percentage  
- Improve UI/UX  
- Add authentication system  
- Deploy on cloud (Railway / Render)  

