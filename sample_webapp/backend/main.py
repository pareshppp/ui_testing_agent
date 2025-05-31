from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, Any
import json
import os
import uuid
from datetime import datetime

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

class FormData(BaseModel):
    name: str
    email: str
    phone: str
    message: str

@app.post("/api/submit")
async def submit_form(form_data: FormData):
    # Generate a unique filename
    filename = f"data/form_submission_{uuid.uuid4()}.json"
    submission = {
        **form_data.dict(),
        "submitted_at": datetime.now().isoformat()
    }
    
    # Save to file
    with open(filename, "w") as f:
        json.dump(submission, f, indent=2)
    
    # Prepare response
    response_data = {
        "status": "success",
        "message": "Form submitted successfully",
        "data": submission
    }
    
    return JSONResponse(
        content=response_data,
        status_code=200,
        headers={"Content-Type": "application/json"}
    )

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Form API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
