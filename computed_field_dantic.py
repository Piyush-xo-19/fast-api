from pydantic import BaseModel,computed_field;
from typing import List,Dict, Annotated,Optional

class Patient(BaseModel):
    name:str
    weight:float
    height:float
    age:int
    married:Optional[bool]=None
    @computed_field
    @property
    def bmi(self)-> float:
        bmi= self.weight/self.height**2
        return bmi
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
   # print(patient.allergies)
    print(patient.married)
    print("bmi",patient.bmi)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2,"height":1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)    
