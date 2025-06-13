import streamlit as st

st.title("🧮 BMI Calculator")

weight = st.number_input("⚖️ Enter your weight (kg):")
height = st.number_input("📏 Enter your height (cm):")
final_height = (height/100) ** 2  # Convert cm to meters squared

if st.button("🔢 Calculate BMI"):
    bmi = weight / final_height
    st.success(f"🎯 Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.warning("💪 You are underweight! Eat more nutritious foods")
    elif 18.5 <= bmi < 24.9:
        st.info("👍 You have a normal weight! Keep it up")
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ You are overweight! Consider more exercise")
    else:
        st.error("❗ You are obese. Please consult a doctor")