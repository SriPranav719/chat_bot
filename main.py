from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from chat_utils import get_gemini_response

app = FastAPI()

# Temporary memory storage
chat_history = []  

@app.post("/chat")
async def chat(request: Request):
    data = await request.json() #converting the input json message into python dict so that we can access the data
    user_message = data.get("message", "")

    # Call the Gemini API
    reply = await get_gemini_response(user_message) #calling the gemini_response to process the request and fetch the response 

    # appending the chat history in the list 
    chat_history.append({
        "user": user_message,
        "bot": reply
    })

    return JSONResponse(content={"reply": reply}) # 


#here creating a get request to get the chat history, but it gets deleted when the server restarts.
@app.get("/history")
def get_history():
    #endpoint to get and return stored chat history
    return JSONResponse(content={"history": chat_history}) 
