import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.set_page_config(page_title="Student Score Predictor", page_icon="🎓")
st.title("🎓 Student Score Predictor")
st.markdown("Predict a student's **reading score** based on their background and math performance.")
st.divider()

math_score = st.slider("Math Score", 0, 100, 65)
gender = st.selectbox("Gender", ["Female", "Male"])
lunch = st.selectbox("Lunch Type", ["Standard", "Free/Reduced"])
prep = st.selectbox("Test Preparation Course", ["None", "Completed"])
parent_edu = st.selectbox("Parental Level of Education", [
    "Some High School", "High School", "Some College",
    "Associate's Degree", "Bachelor's Degree", "Master's Degree"
])

gender_enc    = 0 if gender == "Female" else 1
lunch_enc     = 1 if lunch == "Standard" else 0
prep_enc      = 0 if prep == "None" else 1
parent_map    = {
    "Some High School": 4,
    "High School": 2,
    "Some College": 5,
    "Associate's Degree": 0,
    "Bachelor's Degree": 1,
    "Master's Degree": 3
}
parent_enc = parent_map[parent_edu]

input_data = np.array([[math_score, gender_enc, lunch_enc, prep_enc, parent_enc]])

st.divider()
if st.button("🔮 Predict Reading Score"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Reading Score: **{prediction:.1f} / 100**")
    if prediction >= 70:
        st.balloons()
        st.info("🏆 This student is predicted to be a high performer!")
    else:
        st.warning("📚 This student may benefit from additional support.")