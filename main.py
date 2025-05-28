from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from chat_utils import get_gemini_response

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    # Call the Gemini API and get full response (non-streaming)
    reply = await get_gemini_response(user_message)

    # Return normal JSON response (no streaming here)
    return JSONResponse(content={"reply": reply})
