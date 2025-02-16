import requests

from source.ai_agents.agent_base import linkedin
from source.ai_agents.linkedin_profile import fetch_founder_profile
# from source.ai_agents.linkedin_company import fetch_company

# class LinkedInAPI:
# 	def __init__(self):
# 		self.profile_api = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile-by-salesnavurl'
# 		self.company_api = 'https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-by-linkedinurl'
# 		self.auth = "6c408a89a8mshc72f172ed737c94p14a60ejsn073b4e8765eb"
#
# 		self.headers = {
# 			"x-rapidapi-key": self.auth,
# 			"x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com"
# 		}
#
# 	def get_founder_info(self, linkedin_url):
# 		querystring = {"linkedin_url": {linkedin_url}
# 			, "include_skills": "true", "include_certifications": "true"
# 			, "include_publications": "true", "include_honors": "true", "include_volunteers": "true"
# 			, "include_projects": "true", "include_patents": "true", "include_courses": "true"
# 			, "include_organizations": "true"}
# 		return requests.get(self.profile_api, headers=self.headers, params=querystring).content
#
# 	def get_company_info(self, linkedin_url):
# 		querystring = {"linkedin_url": {linkedin_url}}
# 		return requests.get(self.company_api, headers=self.headers, params=querystring).content


def fetch_linkedInData(founders_urls):
	founders = []

	for founder_url in founders_urls:

		linkedin_profile, profile = fetch_founder_profile(founder_url)
		founders.append({
				"name": linkedin_profile['data']["full_name"],
				"details": [
					{
						"question": "How many years of industry-specific experience does the founder have?",
						"answer": f"{profile['years_of_industry_experience']} years in software development."
					},
					{
						"question": "Has the founder worked at reputable companies (e.g., Fortune 500, unicorns)?",
						"answer": f"{profile['reputable_companies']}"
					},
					{
						"question": "How many previous leadership roles (CEO, CFO, etc.) has the founder held?",
						"answer": f"{profile['leadership_roles']}"
					},
					{
						"question": "Are there employment gaps or frequent job changes (>3 roles in 5 years)?",
						"answer": f"{profile['additional_context']}"
					}]})
	return founders

if __name__ == '__main__':
	founders = fetch_linkedInData(["https://www.linkedin.com/in/sunnymay/"
		, "https://www.linkedin.com/in/daniel-villegas-laguna/"])