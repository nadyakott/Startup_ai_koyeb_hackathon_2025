import requests

class CrunchbaseAPI:
	def __init__(self):
		self.headers = {
			"x-rapidapi-key": "6c408a89a8mshc72f172ed737c94p14a60ejsn073b4e8765eb",
			"x-rapidapi-host": "crunchbase4.p.rapidapi.com",
			"Content-Type": "application/json"
		}

		self.url = "https://crunchbase4.p.rapidapi.com/company"

	def fetch_company_details(self, company_name):
		querystring = { "company_domain": company_name }
		return requests.get(self.url, headers=self.headers, params=querystring).content