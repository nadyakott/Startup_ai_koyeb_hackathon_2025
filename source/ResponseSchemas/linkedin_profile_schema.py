import os
import json
from typing import List, Optional
from pydantic import BaseModel, HttpUrl, conint

# Define LinkedIn profile response model
class LinkedInProfile(BaseModel):
    full_name: str
    headline: str
    location: str
    industry: str
    company_name: Optional[str]
    company_website: Optional[HttpUrl]
    company_employee_range: Optional[str]
    company_industry: Optional[str]
    year_founded: Optional[conint(ge=1800)]
    linkedin_url: HttpUrl
    experiences: List[dict]
    educations: List[dict]
    skills: List[str]
    connection_count: conint(ge=0)

class LinkedInAnalysis(BaseModel):
    years_of_industry_experience: conint(ge=0)
    reputable_companies: str
    leadership_roles: conint(ge=0)
    job_changes: conint(ge=0)
    additional_context: Optional[str]