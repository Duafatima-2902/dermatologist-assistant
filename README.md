# dermatologist-assistant
# 🩺 Your Personal Dermatologist

A FastAPI + Gemini AI-powered chatbot that answers skin-related queries.

## How to Run

1. Clone the repo
2. Create `.env` file with your GEMINI_API_KEY
3. Install dependencies:
pip install -r requirements.txt
4. Run the backend:
uvicorn main:app --reload
5. Open `frontend.html` in your browser

## Example Question

> Why is my skin dry in winter?

## Powered by
- Google Gemini API
- FastAPI
- HTML + CSS + JS Frontend

## Demo Preview

<img width="419" height="114" alt="image" src="https://github.com/user-attachments/assets/938c77af-1332-431a-be8b-edd9a119dff9" />

<img width="954" height="471" alt="image" src="https://github.com/user-attachments/assets/6f85003a-0c38-455b-bdb7-d5bda9571052" />

Tested the /ask endpoint using FastAPI's Swagger UI at http://127.0.0.1:8000/docs.
Confirmed that the API accepts skin-related queries and returns accurate AI-generated responses.
The test validates successful integration and correct schema handling.
<img width="950" height="454" alt="image" src="https://github.com/user-attachments/assets/d36c4393-b1bb-4b04-be9a-a7a24329b23d" />
