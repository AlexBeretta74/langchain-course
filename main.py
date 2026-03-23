from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilyResearch


llm = ChatOpenAI()
tools = [TavilyResearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job posting for an ai engineer using langchain in Turin, Italy and list their details")})
    print(result)

if __name__ == "__main__":
    main()
