from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Request body schema
class LogInput(BaseModel):
    log_text: str

# POST endpoint to analyze logs
@app.post("/analyze")
async def analyze_log(data: LogInput):
    try:
        print(f"Sending log to OpenAI: {data.log_text}")

        # Use GPT-3.5 Turbo (widely available and fast)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert incident responder. Analyze logs and suggest possible root causes and next steps."
                },
                {
                    "role": "user",
                    "content": data.log_text
                }
            ]
        )

        print("OpenAI response received.")
        return {"summary": response['choices'][0]['message']['content']}

    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(status_code=500, detail=str(e))
