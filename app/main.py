from fastapi import FastAPI

app = FastAPI(title="College ERP Backend")

@app.get("/")
def home():
    return {"message": "College ERP Backend is running"}