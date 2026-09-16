from pydantic import BaseModel, Field


class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    city: str
    age: int = Field(ge=18)