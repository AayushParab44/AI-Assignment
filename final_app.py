from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import io

import mysql.connector

import torch 
from PIL import Image 
     
# from torch import nn 
# from torchvision import datasets,transforms
from torchvision import transforms


app = Flask(__name__)

#device setting
device = "cuda" if torch.cuda.is_available() else "cpu"

#import the MNIST model arch.
from model_architecture import MNIST_model

#Load the model
model = torch.load(r'my_model.pth',map_location=device)

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    # host='db',
    port=3306,
    user="root",
    password="aayush12@",
    database="your_database_name"
)
cursor = db_connection.cursor()

# Function to log predictions to MySQL database
def log_predictions(image_path, predictions):
    cursor.execute("INSERT INTO prediction_logs (image_path, predictions) VALUES (%s, %s)",
                   (image_path, predictions.item()))
    db_connection.commit()

# Function to preprocess image and make predictions
def predict_image(img):
       transform = transforms.Compose([transforms.PILToTensor(),transforms.ConvertImageDtype(torch.float)]) 
       img = img.resize((28,28))
       img_tensor = transform(img)  #convert image from PIL to tensor(needed as input for the model)
       img=img_tensor
       print(img.shape)
       model_pred_logits = model(img.unsqueeze(dim=0).to(device)) # make sure image is right shape + on right device
       model_pred_probs = torch.softmax(model_pred_logits, dim=1)
       model_pred_label = torch.argmax(model_pred_probs, dim=1)
       print(model_pred_label)

       return model_pred_label

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        #Incase upload button is clicked without selecting any file
        if file.filename == '':
            return render_template('index.html', error='No selected file')

        try:
            # Read image from file and make predictions
            img = Image.open(io.BytesIO(file.read()))

            predictions = predict_image(img)
            log_predictions(file.filename, predictions)

            return render_template('index.html', predictions=predictions)
        
        except Exception as e:
            return render_template('index.html', error=f'Error processing image: {e}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
