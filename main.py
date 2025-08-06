from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise HTTPException(status_code=500, detail="GEMINI_API_KEY not set.")

# Configure Gemini
genai.configure(api_key=api_key)

# Define model with system instruction
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=(
        "You are a professional dermatologist. Answer skin-related questions "
        "with clear, medically accurate, and empathetic explanations. "
        "Suggest over-the-counter options if applicable, and recommend seeing "
        "a doctor if necessary. Avoid diagnosing serious issues definitively."
    )
)

# Define app
app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, use specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class SkinQuery(BaseModel):
    question: str

# Endpoint: /ask
@app.post("/ask")
async def ask_dermatologist(query: SkinQuery):
    try:
        response = model.generate_content(query.question)
        return {"response": response.text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
