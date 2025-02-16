import requests

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