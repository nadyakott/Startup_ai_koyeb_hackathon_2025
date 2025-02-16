import requests
from agent_base import agent

questions = [
	"How many years of industry-specific experience does the founder have?",
	"Has the founder worked at reputable companies (e.g., Fortune 500, unicorns)?",
	"How many previous leadership roles (CEO, CFO, etc.) has the founder held?",
	"Are there employment gaps or frequent job changes (>3 roles in 5 years)?"
]

def extract_data(founder_data):
    responses = {}
    for question in questions:
                response = agent.run(f"Based on this data {founder_data}, answer the question {question}")
                responses[question] = response
    return responses


# res = agent.run(f"Based on {founder_data}, answer the questions: {questions}.")