from fastapi import FastAPI
import blob

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/text/{text}")
def get_text(text :str):
    sub = blob.getSubjectivity(text)
    pol = blob.getPolarity(text)
    return { 
        "Subjectivity" : sub,
        "Polarity"     : pol
    }