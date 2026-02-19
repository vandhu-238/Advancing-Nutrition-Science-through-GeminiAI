import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_nutrition(food):
    prompt = f"""
    Give detailed nutrition information for {food}.
    Include calories, protein, carbs, fats, vitamins and minerals.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


def get_meal_plan(age, weight, goal, diet, allergies):
    prompt = f"""
    Create a healthy 7-day meal plan.

    Age: {age}
    Weight: {weight}
    Goal: {goal}
    Diet type: {diet}
    Allergies: {allergies}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text



def get_coaching(question):
    prompt = f"Act as a professional nutrition coach and answer: {question}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
