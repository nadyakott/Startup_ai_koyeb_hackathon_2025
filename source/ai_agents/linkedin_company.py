from agent_base import agent, linkedin
from source.api.linkedin import LinkedInAPI
from json_output_format import COMPANY_OUTPUT_JSON_FORMAT

linkedin = LinkedInAPI()

def fetch_company(company_link):
    responses = {}
    output = linkedin.get_company_info(company_link)

    # response = agent.run(f"Based on this data {output}, sum up information about company. Use as an output the following json format {COMPANY_OUTPUT_JSON_FORMAT}")
    response = agent.run(f"Based on this data {output}, sum up information about company.")
    return response

if __name__ == '__main__':
    company_link = 'https://www.linkedin.com/company/ex-corp/'
    res = fetch_company(company_link)
    print(res)