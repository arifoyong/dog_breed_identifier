from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
import shutil
from class_names import CLASS_NAMES

print(tf.__version__)

model = tf.keras.models.load_model('models/inception_8030.h5')
origins = [ "http://localhost:3001",
            "http://dogbreed.oyong.tk"
          ]

img_height, img_width = 224, 224


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def decode_img(img):
  img = tf.io.decode_jpeg(img, channels=3)
  return tf.image.resize(img, [img_height, img_width])


@app.get('/api')
def read_api():
  return {"message": "Hello World"}

@app.get('/class')
def read_api():
  return {"class": CLASS_NAMES}

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
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