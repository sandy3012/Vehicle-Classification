from flask import Blueprint, render_template, request, send_from_directory
import tensorflow as tf
import base64
import re
import numpy as np
import os

classify = Blueprint('classify', __name__)

model = None

img_height = 192
img_width = 192
channels = 3
label_names = ['Air Vehicles', 'Road vehicles', 'Water Vehicles', 'amphibious vehicles']

def load_model():
    global model
    path = './static/model/model2.h5'
    model = tf.keras.models.load_model(path)

# Preprocess an image
def preprocess_image(image):
    image = tf.image.decode_jpeg(image, channels=channels)
    image = tf.image.resize(image, [img_height, img_width])
    image /= 255.0  # normalize to [0,1] range

    return image

# Read the image from path and preprocess
def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    return preprocess_image(image)

# Predict & classify image
def classify_image(model, image_path):

    preprocessed_imgage = load_and_preprocess_image(image_path)
    preprocessed_imgage = tf.reshape(preprocessed_imgage, (1,img_height ,img_width ,3))

    prob_list = model.predict(preprocessed_imgage)
    prob = max(prob_list[0])
    print(prob_list, prob)
    output_index = list(prob_list[0]).index(prob)
    label = label_names[output_index]
    
    return label, round((prob * 100), 2)

@classify.route("/classify", methods=['POST','GET'])
def render_classify():
    if model is None:
        load_model()
    if request.method == 'POST':
        file = request.files["image"]
        upload_image_path = os.path.join('uploads/', file.filename)
        file.save(upload_image_path)

        label, prob = classify_image(model, upload_image_path)

    # img_raw = parse_image(request.get_data())

    # img_preprocessed = preprocess_image(img_raw)
    # outputs = model.predict(tf.expand_dims(img_preprocessed, 0))[0]
    # pred_class = label_names[np.argmax(outputs)]

    return render_template('classify.html', image_file_name = file.filename, label = label, prob = prob)

@classify.route('/classify/<filename>')
def send_file(filename):
    return send_from_directory('uploads', filename)