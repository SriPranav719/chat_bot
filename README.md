#  Chatbot Project – FastAPI + LLM Integration

This project builds a chatbot backend using **FastAPI** and a **Large Language Model (LLM)** like OpenAI GPT .

##  Goals

- Build an API with FastAPI  
- Connect the API to an LLM using its API  
- Send messages to and get replies from the LLM  
- Handle requests smoothly with an async backend  


##  Requirements

### 1. Operating System
- Windows 10 or 11, macOS, or Linux

### 2. Python
- Python 3.8 or newer
- `pip` to install packages
- Use a virtual environment like `venv` 

### 3. Python Libraries

- Run this command to install all required libraries:

```bash
   pip install fastapi uvicorn httpx python-dotenv

```

### 4. LLM API (The chatbot’s brain)

- Choose one LLM provider:  
  - Google Gemini  
  - Anthropic Claude  
  - OpenAI GPT  
  - MCP  
- Get an API key from the provider  
- Check their documentation for API usage  

### 5. Tools to Use

- **VS Code** – for writing your code  
- **Git** – to manage code versions  
- **Thunder Client** (VS Code extension) 

### 6. Running the Project

1. Clone the repository or create your project folder.  
2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv\Scripts\activate  # Windows


##  Summary Checklist
-------------------------------------------------------------------------------
| Component             | Requirement / Action                                |
|-----------------------|-----------------------------------------------------|
| OS                    | Windows 10+, macOS, or Linux                        |
| Python                | Version 3.8+                                        |
| Libraries             | fastapi, uvicorn, httpx, python-dotenv              |
| Virtual Environment   | Use `venv`                                          |
| LLM API Access        | OpenAI                                              |
| API Key               | Store securely in `.env` file                       |
| Code Editor           | VS Code                                             |
| Git                   | Installed and initialized in project                |
| API Testing Tools     | Thunder-Client                                      |
| Project Folder Setup  | `main.py`, `.env`, `requirements.txt` structured    |
| Internet              | Stable connection required for LLM API usage        |
-------------------------------------------------------------------------------
