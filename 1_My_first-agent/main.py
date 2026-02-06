# from openai._extras._common import format_instructions
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic   
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
# from langchain.agents import AgentExecutor
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage

import os


load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("GROQ_API_KEY")
    )

# parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# prompt = ChatMessagePromptTemplate.from_messages(
#     [
#         (
#             "System",
#             """
#             You are a research assisstant that will help generate a research paper.
#             Answer the user query and use neceessary tools.
#             Wrap the output in this format and provide no other text\n{format_instructions}
#             """,
#         ),
#         ("placeholder", "{chat_history}"),
#         ("human", "{query}"),
#         ("placeholder", "{agent_scratchpad}")
#     ]
# ).partial(format_instructions=parser.get_format_instructions())

# Define your custom system prompt
system_prompt = """You are a helpful research assistant that helps generate research papers.
Answer the user's questions accurately and use the available tools when necessary.
Be concise and professional in your responses."""

# llm2 = ChatAnthropic(model="claude-3-5sonnet-20241022")

# response = llm.invoke("What is the meaning of life?")
# print(response.content)


# agent = create_react_agent(
#     llm=llm,
#     prompt=prompt,
#     tools=[]
# )

# agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
# raw_response = agent_executor.invoke({"query": "What is the capital of Tamil Nadu?"})
# print(raw_response)


agent = create_react_agent(
    llm,
    tools=[]
)

raw_response = agent.invoke({"messages": [("human", "What is the capital of Tamil Nadu?")]})
# print(raw_response)
print(raw_response['messages'][-1].content)