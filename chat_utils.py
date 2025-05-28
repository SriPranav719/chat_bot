import os
import httpx
import json
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def get_gemini_response(user_message: str):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [{"text": user_message}]
            }
        ]
    }

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        try:
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            return text
        except Exception as e:
            print("Error parsing response:", e)
            return "Error parsing response"
