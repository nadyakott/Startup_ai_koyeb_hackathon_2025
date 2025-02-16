import requests
from smolagents import Tool, CodeAgent, LiteLLMModel, DuckDuckGoSearchTool
# from mcp import StdioServerParameters
# from langchain_community.tools import DuckDuckGoSearchTool
import os

search_tool = DuckDuckGoSearchTool()

os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")

class LinkedInAPI:
	def __init__(self):
		self.profile_api = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile-by-salesnavurl'
		self.company_api = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-by-linkedinurl'
		self.auth = "6c408a89a8mshc72f172ed737c94p14a60ejsn073b4e8765eb"

		self.headers = {
			"x-rapidapi-key": self.auth,
			"x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com"
		}

	def get_founder_info(self, linkedin_url):
		querystring = {"linkedin_url": {linkedin_url}
			, "include_skills": "true", "include_certifications": "true"
			, "include_publications": "true", "include_honors": "true", "include_volunteers": "true"
			, "include_projects": "true", "include_patents": "true", "include_courses": "true"
			, "include_organizations": "true"}
		return requests.get(self.profile_api, headers=self.headers, params=querystring).content

	def get_company_info(self, linkedin_url):
		querystring = {"linkedin_url": {linkedin_url}}
		return requests.get(self.company_api, headers=self.headers, params=querystring).content

class LinkedInTool(Tool):
	name = "linkedin tool"
	description = "Returns profile info"
	inputs = {
		"task": {
			"type": "string",
			"description": "Returns profile info"
		}
	}
	output_type = "string"

	def forward(self, task: str):
		return LinkedInAPI.get_founder_info(linkedin_url="https://www.linkedin.com/in/sunnymay/")

questions = [
	"How many years of industry-specific experience does the founder have?",
	"Has the founder worked at reputable companies (e.g., Fortune 500, unicorns)?",
	"How many previous leadership roles (CEO, CFO, etc.) has the founder held?",
	"Are there employment gaps or frequent job changes (>3 roles in 5 years)?"
]

linkedin = LinkedInAPI()
# founder_data = linkedin.get_founder_info(linkedin_url="https://www.linkedin.com/in/sunnymay/")

litellm_model = LiteLLMModel(model_id="anthropic/claude-3-5-haiku-latest")
agent = CodeAgent(tools=[search_tool], model=litellm_model)

# res = agent.run(f"Based on {founder_data}, answer the questions: {questions}.")

res = agent.run(f"Can you tell me about company cs.money")
print(res)

#
# 	def retrive_founder_info(self):
# 		for question in self.questions:
# 			response = agent.ask(f"Based on this data {founder_data}, {question}")
# 			responses[question] = response
