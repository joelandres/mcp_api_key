import os
from datetime import datetime
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MCP_API_KEY")

app = FastAPI(title="Example MCP Server")


# ---- Authentication Dependency ----
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


# ---- MCP Tool Input Schema ----
class PatientAgeRequest(BaseModel):
    birth_date: str  # Format: YYYY-MM-DD


# ---- MCP Tool Endpoint ----
@app.post("/tools/get_patient_age")
def get_patient_age(
    request: PatientAgeRequest,
    x_api_key: str = Header(...)
):
    verify_api_key(x_api_key)

    try:
        birth_date = datetime.strptime(request.birth_date, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day)
        )

        return {
            "result": {
                "age": age
            }
        }

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid birth_date format")