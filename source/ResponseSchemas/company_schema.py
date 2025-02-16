from pydantic import BaseModel, HttpUrl, conint
from typing import List
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import json
import os

# Define the response model
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

# # Example company data
# company_data = {
#     "company_name": "Deep Knowledge Analytics",
#     "year_founded": 2018,
#     "hq_city": "London",
#     "hq_country": "GB",
#     "employee_count": 11,
#     "industry": "Research Services",
#     "description": (
#         "DeepTech industry analytics, benchmarking and forecasting renowned for its analytics and strategic "
#         "consulting services on AI and DeepTech. Its Pharma Division is the leading provider of deep industry "
#         "intelligence for the AI in Pharma sector."
#     ),
#     "specialties": [
#         "AI", "artificial intelligence", "big data", "DeepTech", "FinTech",
#         "data science", "machine learning", "GovTech", "InvestTech", "Blockchain",
#         "drug discovery", "pharma", "longevity", "aging", "healthspan", "geroscience",
#         "agetech", "preventive medicine", "big data analysis", "data"
#     ],
#     "website": "https://www.dka.global/",
#     "linkedin_url": "https://www.linkedin.com/company/dkaglobal/",
#     "locations": ["London, GB", "San Francisco, US"],
#     "funding_round": "Seed",
#     "funding_year": 2019
# }
#
# # Validate data against the model
# company = CompanyInfo(**company_data)
#
# # Initialize LangChain model (using OpenAI, you can replace with another LLM)
# llm = ChatOpenAI(model_name="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))
#
# # Generate a response using LangChain
# messages = [
#     SystemMessage(content="You are an AI expert in company analysis."),
#     HumanMessage(content=f"Analyze this company data: {company.json()}")
# ]
#
# response = llm(messages)
#
# # Print or process the response
# print(json.dumps(response.dict(), indent=4))
