from typing import List, Optional
from pydantic import BaseModel

class ExperienceItem(BaseModel):
    company: str
    role: str
    duration: str
    location: Optional[str] = None
    bullets: List[str]

class ProjectItem(BaseModel):
    title: str
    description: str
    technologies: List[str]
    impact: Optional[str] = None
    links: Optional[List[str]] = None

class EducationItem(BaseModel):
    degree: str
    institution: str
    graduation: str
    gpa: Optional[str] = None

class ResearchPaperItem(BaseModel):
    title: str
    publication: str
    year: str
    authors: Optional[List[str]] = None

class ResumeContent(BaseModel):
    summary: str
    skills: dict  # Or create a Skills model
    experience: List[ExperienceItem]
    projects: List[ProjectItem]
    education: List[EducationItem]
    research_papers: List[ResearchPaperItem]