<<<<<<< HEAD
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
import shutil

from class_names import CLASS_NAMES

app = FastAPI()
model = tf.keras.models.load_model('models/inception_8030.h5')

origins = [ "http://localhost:3001",
            "http://dogbreed.oyong.tk"
          ]

img_height, img_width = 224, 224
=======
from typing import Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from class_names import CLASS_NAMES
import aiofiles
from fastai.vision import *

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://dogbreed.oyong.tk"
]
>>>>>>> 82d10738b19dc75eaa5f5a03cdc8a65924b99513

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
def decode_img(img):
  img = tf.io.decode_jpeg(img, channels=3)
  return tf.image.resize(img, [img_height, img_width])

=======
>>>>>>> 82d10738b19dc75eaa5f5a03cdc8a65924b99513
@app.get('/api')
def read_api():
  return {"message": "Hello World"}

@app.get('/class')
def read_api():
  return {"class": CLASS_NAMES}

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
<<<<<<< HEAD
  tempFile = 'tmp/image.jpg'

  with open(tempFile, "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)

  img_file = tf.io.read_file(tempFile)
  img_jpg = decode_img(img_file)
  prob_score = model.predict(np.expand_dims(img_jpg, 0))
  prob_score = prob_score[0]
  
  pred_id = np.argmax(prob_score)
  sorted_score = np.argsort(prob_score)[::-1]
  top10_result  = [{CLASS_NAMES[i]: float(prob_score[i])} for i in sorted_score[:10]]

  resp = {'prediction': CLASS_NAMES[pred_id],
          "probability": float(np.max(prob_score)),
          "top10": top10_result}

  return resp
=======
  dogBreedModel = load_learner(path='models', file='model_resnet50_08909.pkl')

  tempFile = 'tmp/image.jpg'
  img = await file.read()

  print("receive file:", file.filename)
  async with aiofiles.open(f"{tempFile}", "wb") as f:
    await f.write(img)

  imgToPredict = open_image(tempFile)
  pred_class, pred_idx, outputs = dogBreedModel.predict(imgToPredict)
  pred_id = pred_idx.numpy().item()
  conf_lvl = float(outputs.numpy().max())

  sortedOutputs = np.argsort(outputs.numpy())
  top10Outputs = sortedOutputs[::-1][:10]
  top10  = [{CLASS_NAMES[i]: outputs[i].numpy().item()} for i in top10Outputs]

  resp = {'prediction': CLASS_NAMES[pred_id],
          "probability": conf_lvl,
          "top10": top10}

  return resp
>>>>>>> 82d10738b19dc75eaa5f5a03cdc8a65924b99513
