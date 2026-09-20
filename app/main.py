from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, constr
from typing import List, Optional
from datetime import datetime
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Property Management API")

class PropertyBase(BaseModel):
    id: str
    customer_name: str
    customer_mobile: constr(min_length=10, max_length=15)
    property_name: str
    property_type: str
    status: str = "NEW"

class PropertyResponse(PropertyBase):
    created_at: datetime
    class Config:
        orm_mode = True

@app.post("/properties", response_model=PropertyResponse, status_code=status.HTTP_201_CREATED)
def create_property(prop: PropertyBase, db: Session = Depends(database.get_db)):
    db_prop = db.query(models.PropertyRecord).filter(models.PropertyRecord.id == prop.id).first()
    if db_prop:
        raise HTTPException(status_code=400, detail="ID already registered")
    
    new_prop = models.PropertyRecord(**prop.dict())
    db.add(new_prop)
    db.commit()
    db.refresh(new_prop)
    return new_prop

@app.get("/properties/{id}", response_model=PropertyResponse)
def get_property(id: str, db: Session = Depends(database.get_db)):
    prop = db.query(models.PropertyRecord).filter(models.PropertyRecord.id == id).first()
    if not prop:
        raise HTTPException(status_code=404, detail="Record not found")
    return prop

@app.get("/properties", response_model=List[PropertyResponse])
def list_properties(status: Optional[str] = None, db: Session = Depends(database.get_db)):
    query = db.query(models.PropertyRecord)
    if status:
        query = query.filter(models.PropertyRecord.status == status)
    return query.all()

@app.delete("/properties/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_property(id: str, db: Session = Depends(database.get_db)):
    prop = db.query(models.PropertyRecord).filter(models.PropertyRecord.id == id).first()
    if not prop:
        raise HTTPException(status_code=404, detail="Record not found")
    db.delete(prop)
    db.commit()
    return None