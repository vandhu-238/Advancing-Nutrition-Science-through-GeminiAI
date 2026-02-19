import streamlit as st
from ai_engine import get_nutrition, get_meal_plan, get_coaching

st.set_page_config(page_title="NutriGen AI", layout="wide")

st.title("🥗 Advancing Nutrition Science through GeminiAI")

menu = st.sidebar.radio(
    "Navigation",
    ["Nutrition Analyzer", "Meal Planner", "Virtual Coach"]
)

if menu == "Nutrition Analyzer":
    st.header("Get Nutritional Information")

    food = st.text_input("Enter food item")

    if st.button("Analyze"):
        if food:
            result = get_nutrition(food)
            st.write(result)
        else:
            st.warning("Enter food")

elif menu == "Meal Planner":
    st.header("Personalized Meal Planner")

    age = st.number_input("Age", 10, 100)
    weight = st.number_input("Weight")
    goal = st.selectbox("Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])
    diet = st.selectbox("Diet", ["Veg", "Non-Veg", "Vegan"])
    allergies = st.text_input("Allergies")

    if st.button("Generate Plan"):
        plan = get_meal_plan(age, weight, goal, diet, allergies)
        st.write(plan)

elif menu == "Virtual Coach":
    st.header("AI Nutrition Coach")

    question = st.text_area("Ask your question")

    if st.button("Get Advice"):
        advice = get_coaching(question)
        st.write(advice)
