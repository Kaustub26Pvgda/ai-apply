from pydantic import BaseModel
from typing import List

class ResumeContent(BaseModel):
    summary: str
    skills: List[str]
    experience: List[dict]
    projects: List[dict]
    education: List[dict]
    research_papers: List[dict]
