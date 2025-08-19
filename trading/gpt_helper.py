import os

import openai
from dotenv import load_dotenv

load_dotenv()


class GPTExplainer:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def explain(self, decision: str, price: float) -> str:
        prompt = f"Explica por qué un bot decidiría '{decision}' con un precio de {price} USD."
        response = openai.ChatCompletion.create(
            model="gpt-4", messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
