from pydantic import BaseModel, StrictInt
from typing import List, Dict
import json

def load_data():
    with open("patient1.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("patient1.json", "w") as f:
        json.dump(data, f, indent=4)

class Patient(BaseModel):
    name: str
    age: StrictInt   #  prevents strings like "30"
    city: str
    gender: str
    height: float
    weight: float
    bmi: float
    verdict: str
    allergies: List[str]
    contact_details: Dict[str, str]


def insert_patient(patient_info):
    data = load_data()
    patient_id = f"P{len(data)+1:03}"   # Generate new ID like P006
    data[patient_id] = patient_info
    save_data(data)
    print("Patient inserted successfully!")


# Sample data for insertion
patient_info = {
    "name": "Your Name",
    "city": "Your City",
    "age": 25,
    "gender": "male",
    "height": 1.72,
    "weight": 68,
    "bmi": 22.99,
    "verdict": "Normal",
    "contact_details": {
        "phone": "9876001122",
        "email": "your.email@example.com"
    },
    "allergies": ["Peanuts", "Dust"]
}

# Validate using Pydantic before inserting
patient_1 = Patient(**patient_info)
insert_patient(patient_1.model_dump())   #  Use model_dump() to convert to dict

# Wrong data: age as string → should raise error
patient_info_ = {"name": "nitish", "age": "30"}
patient_2 = Patient(**patient_info_)   #  This will now raise a validation error
