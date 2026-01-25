# Main orchestration script for agent pipeline
# Uses FastAPI to expose endpoints for Chrome extension

from fastapi import FastAPI, Request
from agents.jd_agent import extract_jd
from agents.resume_strategy_agent import plan_resume_strategy
from agents.composer_agent import compose_resume
import json

app = FastAPI()

@app.post("/generate_resume")
async def generate_resume(request: Request):
    data = await request.json()
    job_source = data.get("job_source")
    candidate_profile = data.get("candidate_profile")
    # Step 1: Extract JD
    jd_object = extract_jd(job_source)
    # Step 2: Plan resume strategy
    resume_strategy = plan_resume_strategy(jd_object)
    # Step 3: Compose resume
    resume_content = compose_resume(candidate_profile, resume_strategy)
    # TODO: Convert resume_content to PDF and return
    return {"resume_content": resume_content}
