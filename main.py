from fastapi import FastAPI,Path
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

@app.get("/patient/{patient_id}") #this is known as path param means to add dynamic path 
def view_patient(patient_id:str=Path(... ,description="ID OF THE PATIENT IN DB ",example="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return{"message":"patient id not found enter a valid patient id "}