# Main orchestration script for agent pipeline
# Uses FastAPI to expose endpoints for Chrome extension


from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from agents.jd_agent import extract_jd
from agents.resume_strategy_agent import plan_resume_strategy
from agents.composer_agent import compose_resume
import json
import logging


app = FastAPI()\

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO)


@app.post("/generate_resume")
async def generate_resume(request: Request):
    try:
        data = await request.json()
    except Exception as e:
        logging.error(f"Invalid JSON input: {e}")
        raise HTTPException(status_code=400, detail="Invalid JSON input.")

    job_source = data.get("job_source")
    candidate_profile = data.get("candidate_profile")

    if not job_source or not candidate_profile:
        raise HTTPException(status_code=422, detail="Missing required fields: job_source and candidate_profile.")

    try:
        # Step 1: Extract JD
        jd_object = extract_jd(job_source)
    except (ValidationError, Exception) as e:
        logging.error(f"JD extraction failed: {e}")
        raise HTTPException(status_code=500, detail=f"JD extraction failed: {str(e)}")

    try:
        # Step 2: Plan resume strategy
        resume_strategy = plan_resume_strategy(jd_object)
    except (ValidationError, Exception) as e:
        logging.error(f"Resume strategy planning failed: {e}")
        raise HTTPException(status_code=500, detail=f"Resume strategy planning failed: {str(e)}")

    try:
        # Step 3: Compose resume
        resume_content = compose_resume(candidate_profile, resume_strategy)
    except (ValidationError, Exception) as e:
        logging.error(f"Resume composition failed: {e}")
        raise HTTPException(status_code=500, detail=f"Resume composition failed: {str(e)}")

    return {"resume_content": resume_content}
