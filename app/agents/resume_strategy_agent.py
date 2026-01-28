# Resume Strategy Agent using Agno
from agno.agent import Agent
import logging
from app.schemas.strategy_schema import ResumeStrategy

RESUME_STRATEGY_PROMPT = """
You are a resume strategy planner.

Given a structured job description, decide how a candidate’s resume should be organized for maximum relevance and ATS alignment.

Rules:
1. Do not assume candidate background.
2. Base decisions only on job requirements and role expectations.
3. Prefer clarity and relevance over completeness.
4. Avoid unnecessary sections for the role.

Output a resume strategy strictly following the schema given. Do not generate resume content.

This is the input schema that you will recieve:
{
	"job_description": {}
}

This is the resume strategy object that you have to return:
{
	"target_role": "",
	"seniority": "",
	"sections_to_include": [],
	"sections_to_deprioritize": [],
	"skill_emphasis": [],
	"project_priority_tags": [],
	"include_research": true,
	"quantification_preference": "low | medium | high",
	"max_pages": 1
}

If there are any other relevant fields that you think should be added then add them as well. But do not make up anything or add unnecessary fields
"""

class ResumeStrategyAgent:
	def __init__(self):
		self.agent = Agent(system_prompt=RESUME_STRATEGY_PROMPT)


	def plan(self, job_description):
		try:
			result = self.agent.run({"job_description": job_description})
			if not isinstance(result, dict):
				raise ValueError("ResumeStrategyAgent: Output is not a dict.")
			# Validate with schema
			strategy_obj = ResumeStrategy(**result)
			return strategy_obj.model_dump()
		except Exception as e:
			logging.error(f"ResumeStrategyAgent error: {e}")
			raise RuntimeError(f"Resume strategy planning failed: {e}")

def plan_resume_strategy(jd_object):
	return ResumeStrategyAgent().plan(jd_object)
