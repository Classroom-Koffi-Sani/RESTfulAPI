from typing import List, Optional

from pydantic import BaseModel

class ContactBase(BaseModel):
    firstname: str
    lastname: Optional[str] = None
    email: Optional[str] = None
    phone_1: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    company_id: int
    employees: List[Contact] = []

    class Config:
        orm_mode = True

class CompanyBase(BaseModel):
    email: Optional[str] = None
    name: str

class CompanyCreate(BaseModel):
    pass

class Company(CompanyBase):
    id: int
    
    class Config:
        orm_mode = True