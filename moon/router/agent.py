from fastapi import APIRouter, Request
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from moon.config.llm_model import model
from moon.schema.agent_schema import AgentModel
from moon.tools.tools_kit import web_search, write_tweet

"""初始化路由"""
agent_router = APIRouter()


@agent_router.post("/exec")
async def agent_exec(request: Request, agent_model: AgentModel):
    """
    agent执行，先进行function call，根据询问的内容，看是否能召回工具
    :param request: 请求
    :param agent_model: 请求参数
    :return:
    """
    # system_prompt = ("You are a very responsible assistant who enjoys helping others solve problems. For any "
    #                  "questions posed, you will provide reasonable and thoughtful responses.. please answer the "
    #                  "question：{messages}")
    # prompt = ChatPromptTemplate.from_messages([
    #     ("system", SystemMessage(content=system_prompt)),
    #     MessagesPlaceholder(variable_name="messages")
    # ])
    # print(prompt)
    tools = [web_search, write_tweet]
    agent_executor = create_react_agent(model, tools)

    for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=agent_model.query)]}
    ):
        print(chunk)
        print("-----")



