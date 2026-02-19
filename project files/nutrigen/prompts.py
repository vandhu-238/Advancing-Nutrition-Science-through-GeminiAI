nutrition_prompt = """
Provide complete nutritional information for the food item below.

Food: {food}

Include:
- Calories
- Protein
- Carbohydrates
- Fat
- Vitamins
- Minerals
- Health benefits
"""

meal_plan_prompt = """
Create a 7-day healthy meal plan.

User Details:
Age: {age}
Weight: {weight}
Goal: {goal}
Diet: {diet}
Allergies: {allergies}

Include:
- Breakfast, Lunch, Dinner
- Simple recipes
- Grocery list
"""

coach_prompt = """
Act as a professional nutrition coach.

User Question:
{question}

Provide practical advice.
"""
