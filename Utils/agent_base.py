
from smolagents import Tool, CodeAgent, LiteLLMModel, DuckDuckGoSearchTool
from linkedInData import LinkedInAPI
# from mcp import StdioServerParameters
# from langchain_community.tools import DuckDuckGoSearchTool
import os



linkedin = LinkedInAPI()
search_tool = DuckDuckGoSearchTool()

os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")

litellm_model = LiteLLMModel(model_id="anthropic/claude-3-5-haiku-latest")

agent = CodeAgent(tools=[search_tool], model=litellm_model)
