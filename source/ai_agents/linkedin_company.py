import json

from click import prompt

from agent_base import agent, linkedin
from json_output_format import COMPANY_OUTPUT_JSON_FORMAT

def fetch_company(company_link):
    linkedin_data = linkedin.get_company_info(company_link)

    prompt = f"""
    Analyze this LinkedIn data:
       {linkedin_data}
       
       
       Return the following schema:
       class CompanyInfo(BaseModel):
            company_name: str
            year_founded: conint(ge=1800)  # Ensure reasonable year
            hq_city: str
            hq_country: str
            employee_count: conint(ge=1)
            industry: str
            description: str
            specialties: List[str]
            website: HttpUrl
            linkedin_url: HttpUrl
            locations: List[str]
            funding_round: str
            funding_year: conint(ge=1800)
    """
    # response = agent.run(f"Based on this data {output}, sum up information about company. Use as an output the following json format {COMPANY_OUTPUT_JSON_FORMAT}")
    response = agent.run(prompt)
    json_data = json.dumps(response)
    return json_data

if __name__ == '__main__':
    company_link = 'https://www.linkedin.com/company/ex-corp/'
    res = fetch_company(company_link)
    print(res)