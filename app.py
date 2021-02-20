import os
from flask import Flask, request, render_template, send_from_directory, redirect,url_for
import cv2
import tensorflow.keras
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator


lst = ['Apple','Blueberry','Tomato']
np.set_printoptions(suppress=True)


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
    # Load the model
    model = tensorflow.keras.models.load_model('keras_model.h5',compile=False)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    folder='images'
    ex=folder+'/'+filename
    image = Image.open(ex)
    img_array=np.array([img_to_array(image)])
    data=preprocess_input(img_array)

    # run the inference
    prediction = model.predict(data)
    print(prediction)
    ############################################
    maxx=max(prediction[0])
    ind = np.where(prediction[0]==maxx)
    result_pred = lst[ind[0][0]]
    ############################################

    return render_template("complete_display_image.html",image_name=filename,result_pred =result_pred)

   
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route('/go back')
def back():
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(port=4555, debug=True)
