from pydantic import BaseModel
from typing import List, Dict, Any


class AgentRequest(BaseModel):
    message: str


class Command(BaseModel):
    type: str
    params: Dict[str, Any]


class AgentResponse(BaseModel):
    message: str
    commands: List[Command]
