from langchain_community.tools import TavilySearchResults
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

from moon.config.llm_model import model


@tool("web_search")
def web_search(query: str) -> str:
    """search with api"""
    search = TavilySearchResults(max_results=2)
    return search.invoke(query)


@tool("twitter_writer")
def write_tweet(content: str) -> str:
    """Base on a piece content, write a tweet"""
    chat = ChatOpenAI(model="gpt-4o-mini")
    message = [
        SystemMessage(
            content="you are a Twitter account operator. you are responsible for writing a tweet base on the content "
                    "given. you should fellow the twitter policy and make sure the twitter nno more than 1400 "
                    "characters"),
        HumanMessage(content=content)
    ]
    response = model.invoke(message)
    return response.content
