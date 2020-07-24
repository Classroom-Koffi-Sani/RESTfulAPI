from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    email = Column(String, index=True)
    phone_1 = Column(String)

    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="employees")


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    phone_1 = Column(String)
    email = Column(String)

    employees = relationship("Contact", back_populates="company")