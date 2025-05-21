from pydantic import BaseModel


class DoneResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
        #from_attributes = True