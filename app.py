import streamlit as st
import pandas as pd
import joblib

# load trained model
import joblib

model = joblib.load("risk_model.pkl")

st.title("Healthcare Risk Stratification App")

st.write("Enter patient details to predict risk level")

# user inputs
age = st.number_input("Age", min_value=0, max_value=100)

gender = st.selectbox("Gender", ["Male", "Female"])

diagnosis = st.selectbox("Diagnosis", [
    "Diabetes","Asthma","Arthritis","COPD",
    "Cancer","Kidney Disease","Stroke","Hypertension"
])

length_of_stay = st.number_input("Length of Stay")

treatment_cost = st.number_input("Treatment Cost")

# encode inputs
gender_val = 1 if gender == "Male" else 0

diagnosis_list = [
    "Diabetes","Asthma","Arthritis","COPD",
    "Cancer","Kidney Disease","Stroke","Hypertension"
]

diagnosis_val = diagnosis_list.index(diagnosis)

# prediction button
if st.button("Predict Risk"):

    input_data = pd.DataFrame(
        [[age, gender_val, diagnosis_val, length_of_stay, treatment_cost]],
        columns=["Age","Gender","diagnosis name","Length of Stay","TreatmentCost"]
    )

    prediction = model.predict(input_data)

    st.success(f"Predicted Risk Level: {prediction[0]}")


#Create a launcher script
import subprocess
import os

# Change working directory to the folder where your app is

# Function to check if Streamlit is already running
#def is_streamlit_running():
 #   for proc in psutil.process_iter(['name', 'cmdline']):
  #      try:
   #         if proc.info['cmdline'] and 'streamlit' in ' '.join(proc.info['cmdline']):
    #            return True
     #   except:
      #      continue
    #return False

# Launch Streamlit only if not running
#if not is_streamlit_running():
 #   subprocess.Popen(["python", "-m", "streamlit", "run", "app.py"])
#else:
   # print("Streamlit app is already running!")
