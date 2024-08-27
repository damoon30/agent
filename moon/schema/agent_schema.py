from typing import Optional

from pydantic import BaseModel


class AgentModel(BaseModel):
    agent_id: int
    query: str
    stream: Optional[bool] = True
