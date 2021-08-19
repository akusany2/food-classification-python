import os
import prediction
import requests
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class URL(BaseModel):
    url: str = ""


@app.get("/")
def read_root():
    return {"CML": "NOICE"}


@app.post("/")
async def read_url(url: URL = None):

    image_name = url.url.split("/")[-1]

    img_data = requests.get(url.url).content
    with open(image_name, "wb") as handler:
        handler.write(img_data)

    model_load = load_model("./model_v1_inceptionV3.h5")
    result = prediction.predict_image(image_name, model_load)
    os.remove(image_name)
    return {"prediction": result}
