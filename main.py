from fastapi import FastAPI,Path,HTTPException,Query
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
        raise HTTPException(status_code=400,detail="Patient not found")

#query parameters 
@app.get("/sort")
def sorted_patients(sortby:str=Query(...,description="sort on the basis of height . weight and bmi "),Order:str=Query(..., description="ASCENDING OR DESCENDING" )):
    valid_sort=["weight","height","bmi"]
    valid_order=["ascending","descending"]
    if sortby not in valid_sort:
        raise HTTPException(status_code=400,detail=" INVALID QUERY") 
    if Order not in valid_order:
        raise HTTPException(status_code=400,detail="ENTER A VALID ORDER")
    data=load_data()
    sorted_order= True if Order=="descending" else False
    sorted_data=sorted(data.values(),key=lambda x: x.get(sortby,0),reverse=sorted_order)
    return sorted_data