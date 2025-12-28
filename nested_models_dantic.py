from pydantic import BaseModel,field_validator,model_validator,Field
from typing import List,Dict,Annotated,Optional
class Address(BaseModel):
    city:str
    pincode:str
    house_no:int
    


class patient(BaseModel):
    age:int
    name:str
    gender: str
    address:Address

Address_dict={"city":"gurgaon","house_no":2,"pincode":"110045"}
Address1=Address(**Address_dict)
print(Address1)

pateint_dict={"age":45,"name":"piyush gupta","gender":"male","address":Address1}  
pateint1=patient(**pateint_dict)
print(pateint1)



# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed 