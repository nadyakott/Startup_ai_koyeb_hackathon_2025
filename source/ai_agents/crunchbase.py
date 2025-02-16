from agent_base import agent, linkedin
from source.api.crunchbase import CrunchbaseAPI
from json_output_format import COMPANY_OUTPUT_JSON_FORMAT

def fetch_company(company_name):
    responses = {}
    crunchbase = CrunchbaseAPI()
    output = crunchbase.fetch_company_details(company_name="anthropic")

    # response = agent.run(f"Based on this data {output}, sum up information about company. Use as an output the following json format {COMPANY_OUTPUT_JSON_FORMAT}")
    # response = agent.run(f"Based on this data {output}, sum up information about company.")
    response = agent.run(f"Tell me about company {company_name}.")
    return response

# if __name__ == '__main__':
#     company_link = 'https://www.linkedin.com/company/ex-corp/'
#     res = fetch_company(company_link)
#     print(res)