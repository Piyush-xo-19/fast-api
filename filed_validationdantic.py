#field validator use krte hai kuch prsnl validation krne ka lye jo hum field func with annoated use ka saath nahi kr paa rahe tha 
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
#making the filed validator to check wether the patient email is in from a custom domain like hdfc and icic 
    @field_validator("email")
    @classmethod
    def email_validation(cls,value):
        valid_domain=["hdfc","icic","axis"]
        domain_name=value.split("@")[-1]
        if domain_name not in valid_domain:
            raise ValueError("enter a valid email")

    @field_validator("name")
    @classmethod
    def transform_name(cls,value):
        return value.upper()


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)
