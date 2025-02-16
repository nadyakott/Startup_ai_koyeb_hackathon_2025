def fetch_CrunchbaseData(company_name, company_url, founders_urls):
    return {
  "crunchbase": {
	"company_name": "Example Corp",
	"started_date": "2020-06-15",
	"funding": [
  	{
    	"question": "What is the total equity funding raised (USD)?",
    	"answer": "$2.5M."
  	},
  	{
    	"question": "Time since last raise?",
    	"answer": "18 months ago."
  	},
  	{
    	"question": "How many unique investors (VCs, angels, corporates) have backed the company?",
    	"answer": "8 unique investors."
  	},
  	{
    	"question": "Has the company participated in accelerators/incubators (e.g., Y Combinator)?",
    	"answer": "Yes, Y Combinator W21 Batch Graduate."
  	},
  	{
    	"question": "How many employees does the company have?",
    	"answer": "25 employees."
  	}
	]
  }
}

