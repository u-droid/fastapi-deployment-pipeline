"""
Fast API APP
"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
def health():
    '''Checks the health of the App'''
    return {"detail":"Success"}

@app.post("/")
def get_info(name:str):
    '''Get Info'''
    return {
        "name":name
    }
