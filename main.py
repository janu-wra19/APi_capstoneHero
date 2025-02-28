from prediction import predict,prepocess, read_image, result_desease
from fastapi import FastAPI, File
import json


# 2. Create the app object
app = FastAPI()

@app.get("/")
def home():
    return {"message': 'Server is Online"}

@app.post("/submitform")
async def Handle_form(eye_file : bytes = File(...)):
    img = read_image(eye_file)
    img = prepocess(img)
    prediction = predict(img)
    return{"upload image success."}

@app.get("/get_result")
def predict_result():
    result = result_desease()
    return {"result": result}
    
@app.get("/article")
def art():
    # Opening JSON file
    f = open('article.json',)
    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    return data

