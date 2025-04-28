from pydantic import BaseModel


class CardboardConfig(BaseModel):
    token: str
    guild_id: int
