import blob
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Welcome to textBlob API"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/text/{text}")
async def get_text(text :str):
    sub = blob.getSubjectivity(text)
    pol = blob.getPolarity(text)
    return { 
        "Subjectivity" : sub,
        "Polarity"     : pol
        }

@app.get("/file/{Month}/{Date}")
async def get_item(Month :str,Date :str):
    location = "gs://tourist-bot-hilapp.appspot.com/"+Month+"/"+Date+'.csv'
    output =  blob.getSubjectivityFile(location)
    print(output)
    return output