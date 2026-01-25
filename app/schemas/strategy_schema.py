from pydantic import BaseModel
from typing import List

class ResumeStrategy(BaseModel):
    target_role: str
    seniority: str
    sections_to_include: List[str]
    sections_to_deprioritize: List[str]
    skill_emphasis: List[str]
    project_priority_tags: List[str]
    include_research: bool
    quantification_preference: str
    max_pages: int
