from pydantic import BaseModel

class Patient(BaseModel): #defining the schema of the databse
    name:str #type validation
    age:int  #type validation
    weight:float


    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight

    def insert_patient(self):
        print(self.name)
        print(self.age)
        print("inserted")

patient_info={"name":"nitish","age":19}
patient_1=Patient(**patient_info)
patient_1.insert_patient() 

patient_info_={"name":"nitish","age":"thirty"}
patient_2=Patient(**patient_info_)#now we have modify the age and its a string now so it must raise an error 