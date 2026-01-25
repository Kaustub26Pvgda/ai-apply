from pydantic import BaseModel
from typing import List

class JobDescription(BaseModel):
    job_title: str = ""
    company: str = ""
    location: str = ""
    employment_type: str = ""
    seniority: str = ""
    role_type: str = ""
    responsibilities: List[str] = []
    required_skills: List[str] = []
    preferred_skills: List[str] = []
    education_requirements: List[str] = []
    keywords: List[str] = []
    industry: str = ""