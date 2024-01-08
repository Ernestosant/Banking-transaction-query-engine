from pydantic import BaseModel


class QueryRequest(BaseModel):
    content : str