# JD Extraction Agent using Agno
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.website import WebsiteTools

import logging
import json
import os
import re
from dotenv import load_dotenv

from app.schemas.jd_schema import JobDescription

JD_AGENT_PROMPT = """
You are a job description extraction agent.

Your task is to extract and normalize information from a job application URL or raw job description text.

RULES:
1. Extract only information explicitly present.
2. Use WebsiteTools to fetch content from URLs when needed.
3. Do not infer candidate suitability.
4. Normalize skills and role types to standard terms.
5. If information is missing, leave fields empty.
6. Preserve factual accuracy.

IMPORTANT CONSTRAINTS:
- Each JSON key must appear EXACTLY ONCE.
- Do not repeat keys.
- Do not repeat list items.
- If a value was already written, do not write it again.

OUTPUT FORMAT (STRICT):
Return ONLY a valid JSON object matching this schema.
Do NOT include markdown, explanations, or extra text.

{
  "job_title": "",
  "company": "",
  "location": "",
  "employment_type": "",
  "seniority": "",
  "role_type": "backend | frontend | fullstack | ml | mobile | research | generalist",
  "responsibilities": [],
  "required_skills": [],
  "preferred_skills": [],
  "education_requirements": [],
  "keywords": [],
  "industry": "",
}
"""

def extract_json_from_md(text: str) -> str:
	"""
	Removes ```json ... ``` or ``` ... ``` markdown formatting from a string.
	"""
	match = re.search(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL)
	if match:
		return match.group(1)
	return text

class JDExtractionAgent:
	def __init__(self):
		load_dotenv()
		google_api_key = os.getenv("GOOGLE_API_KEY")

		self.agent = Agent(
			name="JDExtractionAgent",
			model=Gemini(id="gemini-2.5-flash", api_key=google_api_key),
			system_message=JD_AGENT_PROMPT,
			tools=[
				ReasoningTools(add_instructions=True),
				WebsiteTools(),
			],
			# output_schema=JobDescription,
			markdown=False,
		)


	def extract(self, job_source):
		try:
			input_text = f"""
Job Source:
Type: {job_source['type']}
Value: {job_source['value']}			
"""
			response = self.agent.run(input_text)
			print(response) 	# debug
			
			raw_text = response.content.strip()
			clean_json = extract_json_from_md(raw_text)
			data = json.loads(clean_json)

			jd = JobDescription.model_validate(data)
			return response.content
		
		except json.JSONDecodeError as e:
			logging.error(f"Gemini did not return valid JSON")
			raise RuntimeError(f"Invalid JSON returned by Gemini") from e
		
		except Exception as e:
			logging.error(f"JDExtractionAgent error: {e}")
			raise RuntimeError(f"JD extraction failed: {e}")

def extract_jd(job_source):
	return JDExtractionAgent().extract(job_source)
