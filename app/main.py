from fastapi import FastAPI
from app.database import Base, engine
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="College ERP Backend")

@app.get("/")
def home():
    return {"message": "College ERP Backend is running"}