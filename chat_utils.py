import os
import httpx
import json
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def get_gemini_response(user_message: str):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}" #base endpoint for gemini(API) to generate content, and automatically authorizes the API_KEY

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [{"text" : user_message}]  # actual data where the request is stored.
            }
        ]
    }

    async with httpx.AsyncClient(timeout=30) as client: # timeout=30 so that if the API doesnt responds then it raises a timeout error.
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status() # to catch the exceptions , if 200 OK the app runs flexible, otherwise it raises an exception httpx.HTTPStatusError
        data = response.json()    
        # converting the json to python Dict so that we can extract the data easily 
        try:
            text = data["candidates"][0]["content"]["parts"][0]["text"] #accessing the prompt(actual response)
            
            return text  
        except Exception as e:
            print("Error parsing response:", e)
            return "Error parsing response"
