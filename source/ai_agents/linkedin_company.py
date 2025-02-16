from agent_base import agent



def extract_data(founder_data):
    responses = {}
    for question in questions:
            response = agent.run(f"Based on this data {founder_data}, answer the question {question}")
    return responses