# Resume Composer Agent using Agno
import json
from agno.agent import Agent
import logging
from app.schemas.resume_schema import ResumeContent

COMPOSER_AGENT_PROMPT = """
You are a resume composer.

Your task is to generate tailored resume content using a given candidate knowledge base and a resume strategy.

Rules:
1. Use only information present in the candidate profile.
2. Do not invent skills, experience, or metrics.
3. Emphasize skills and projects specified in the resume strategy.
4. Respect proficiency levels.
5. Quantify impact only when safe and factual.

Output structured resume content only. Do not format as a PDF or add commentary.

This is the input schema that you will recieve:
{
	"candidate_profile": {},
	"resume_strategy": {}
}

This is the structured resume content object that you have to return:
{
	"summary": "",
	"skills": [],
	"experience": [],
	"projects": [],
	"education": [],
	"research_papers": []
}

If there are any other relevant fields that you think should be added then add them as well. But do not make up anything or add unnecessary fields. The output you produce should be easily convertible to PDF format.
"""

class ResumeComposerAgent:
    def __init__(self):
        self.agent = Agent(
            system_prompt=COMPOSER_AGENT_PROMPT,
            response_model=ResumeContent
        )


    def compose(self, candidate_profile, resume_strategy):
        user_message = f"""
Generate resume content using the following:

CANDIDATE PROFILE:
{json.dumps(candidate_profile, indent=2)}

RESUME STRATEGY:
{json.dumps(resume_strategy, indent=2)}

Return only valid JSON matching the schema specified in your instructions.
"""
        try:
            response = self.agent.run(user_message)
            resume_data = json.loads(response) if isinstance(response, str) else response
            resume_obj = ResumeContent(**resume_data)
            return resume_obj.model_dump()
        except Exception as e:
            logging.error(f"ResumeComposerAgent error: {e}")
            raise RuntimeError(f"Resume composition failed: {e}")
