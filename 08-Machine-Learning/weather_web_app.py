import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Setup the Web Page
st.title("🌦️ AI Weather Predictor")
st.write("This app uses a Machine Learning model to predict rain based on humidity.")

# 2. The "Brain" (Your ML Model)
X = np.array([[30], [45], [60], [80], [90]]) 
y = np.array([5, 20, 50, 80, 95])
model = LinearRegression()
model.fit(X, y)

# 3. The Web Interface
# Instead of typing, the user moves a slider!
humidity = st.slider("Select Current Humidity (%)", 0, 100, 50)

# 4. The Prediction Logic
if st.button("Predict Chance of Rain"):
    prediction = model.predict([[humidity]])
    st.success(f"The AI predicts a {prediction[0]:.2f}% chance of rain!")
    
    # Add some fun visual logic
    if prediction[0] > 70:
        st.warning("Better take an umbrella! ☔")
    else:
        st.info("Looks like a clear day! ☀️")
