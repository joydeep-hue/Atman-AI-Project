import os
from groq import Groq

# 1. Connect to the Global Brain (Supreme Intelligence)
client = Groq(api_key="")

def generate_supreme_solution(user_problem):
    # This 'Sutra' tells the AI how to act: as a Dharmic Problem Solver
    system_prompt = "You are the Supreme Intelligence (Veda-Py). Your goal is to provide Dharmic, technical, and actionable solutions to global problems."
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_problem}
        ],
        model="llama-3.3-70b-versatile", # High-speed open-source intelligence
    )
    
    return chat_completion.choices[0].message.content

# Test Example
# print(generate_supreme_solution("How can we stop plastic pollution?"))
