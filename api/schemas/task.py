from typing import Optional

from pydantic import BaseModel, Field
 
class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="醤油を買う")
    
class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskBase):
    id: int
    
    class Config:
        #from_attributes = True
        orm_mode = True

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")
    
    class Config:
        # from_attributes = True
        orm_mode = True
    
    