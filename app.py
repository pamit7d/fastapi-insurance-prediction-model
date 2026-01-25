from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated, Literal
from pydantic import BaseModel, Field, computed_field
import pandas as pd
import pickle



app = FastAPI()

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

tier1 = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier2 = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]




class Insurance_premimum_category(BaseModel):
    age: Annotated[int, Field(ge=0, le=120, description="Age must be between 0 and 120", example=45)]
    weight: Annotated[float, Field(default = None, gt=0, description="Weight in kilograms", example=73.4)]
    height: Annotated[float, Field(default = None, gt=0, description="Height in meters", example=1.7)]
    income_lpa: Annotated[float, Field(default = None, gt=0, description="Income in lakhs per annum", example=5)]
    smoker: Annotated[bool, Field(description="Whether the person is a smoker or not", example=False)]
    city: Annotated[str, Field(description="City of residence", example="New York")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
    
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        else:
            return "senior"
        
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
    
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier1:
            return 1
        elif self.city in tier2:
            return 2
        else:
            return 3
        

@app.post("/predict")
def predict_insurance_premium(data: Insurance_premimum_category):
    
    input_df = pd.DataFrame({
        "age": [data.age],
        "bmi": [data.bmi],
        "income_lpa": [data.income_lpa],
        "smoker": [data.smoker],
        "city_tier": [data.city_tier],
        "occupation": [data.occupation],
        "age_group": [data.age_group],
        "lifestyle_risk": [data.lifestyle_risk]
    })
        
    
    prediction = model.predict(input_df)[0]
    
    return JSONResponse(status_code=200, content={"response": prediction})
