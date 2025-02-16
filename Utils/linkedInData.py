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


def fetch_linkedInData(company_name, company_url, founders_urls):

    
    return {
	"founders": [
  	{
    	"name": "Youssef Ben Mahmoud",
    	"details": [
      	{
        	"question": "How many years of industry-specific experience does the founder have?",
        	"answer": "12 years in software development."
      	},
      	{
        	"question": "Has the founder worked at reputable companies (e.g., Fortune 500, unicorns)?",
        	"answer": "Yes, Microsoft and Oracle."
      	},
      	{
        	"question": "How many previous leadership roles (CEO, CFO, etc.) has the founder held?",
        	"answer": "3 leadership roles (CTO, VP of Engineering, CEO)."
      	},
      	{
        	"question": "Are there employment gaps or frequent job changes (>3 roles in 5 years)?",
        	"answer": "No gaps; consistent career progression."
      	}
    	]
  	},
  	{
    	"name": "Mohamed Khalil Jabri",
    	"details": [
      	{
        	"question": "How many years of industry-specific experience does the founder have?",
        	"answer": "10 years in fintech."
      	},
      	{
        	"question": "Has the founder worked at reputable companies (e.g., Fortune 500, unicorns)?",
        	"answer": "Yes, Stripe and Goldman Sachs."
      	},
      	{
        	"question": "How many previous leadership roles (CEO, CFO, etc.) has the founder held?",
        	"answer": "2 leadership roles (VP of Product, CTO)."
      	},
      	{
        	"question": "Are there employment gaps or frequent job changes (>3 roles in 5 years)?",
        	"answer": "No gaps; steady career growth."
      	}
    	]
  	},
  	{
    	"name": "Founder 3",
    	"details": [
      	{
        	"question": "How many years of industry-specific experience does the founder have?",
        	"answer": "15 years in AI and machine learning."
      	},
      	{
        	"question": "Has the founder worked at reputable companies (e.g., Fortune 500, unicorns)?",
        	"answer": "Yes, Google and DeepMind."
      	},
      	{
        	"question": "How many previous leadership roles (CEO, CFO, etc.) has the founder held?",
        	"answer": "4 leadership roles (Chief Scientist, VP of AI, CTO, CEO)."
      	},
      	{
        	"question": "Are there employment gaps or frequent job changes (>3 roles in 5 years)?",
        	"answer": "No gaps; consistent career trajectory."
      	}
    	]
  	}
	]
  }