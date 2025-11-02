from fastapi import FastAPI
import json
app=FastAPI()
def load_data(): #loading patient data 
    with open("patient.json","r") as f :
        data=json.load(f)
    return data

@app.get("/") 
def hello():
    return {"message":"PATIENT MANAGEMENT API SYSTEM  "}

@app.get("/about")
def about():
    return {"message":" A FULLY FUNCTIONAL API FOR PATIENT RECORD  "}

@app.get("/view")
def view():
    
    return load_data()