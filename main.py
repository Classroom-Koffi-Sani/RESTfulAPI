from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {'Hello': 'World'}

@app.get("/contacts/{contact_id}")
def read_contact(contact_id: int, q: str = None):
    return {"contact_id": contact_id, "q": q}

@app.get("/contacts/", response_model=List[schemas.Contact])
def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contacts = crud.get_contacts(db, skip=skip, limit=limit)
    return contacts

@app.post("/contacts/", response_model=schemas.Contact)
def create_contact (contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    db_contact = crud.get_contact_by_email(db, email=contact.email)
    if db_contact:
        raise HTTPException(status_code=400, detail="Contact déjà enrégistré avec cette adresse email")
    return crud.create_contact(db=db, contact=contact)