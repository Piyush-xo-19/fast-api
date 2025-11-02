from fastapi import FastAPI
app=FastAPI()
@app.get("/") 
def hello():
    return {"message":" this is my 1 end point "}

@app.get("/about")
def yeah():
    return {"message":"hi this is my 2 end point "}