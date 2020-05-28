import numpy as np
import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import data_file
import face_load
import face_processing


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/getPrediction',methods=['POST'])
def getPrediction(): 
    
    output_json = {}
    # check if the post request has the file part
    if 'file' not in request.files:
        output = {"message":"FILE NOT FOUND"}      
        return jsonify(output)
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        output = {"message":"FILE IS EMPTY"}  
        return jsonify(output)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #output = data_file.known_names
    #output = face_processing.process_unknown_faces()
    
    print("---------output-----------")
   
    output_json['post_id'] = request.form['post_id']
    #output_json['faces'] = output
    
    os.remove(os.path.join(UPLOAD_FOLDER,filename))
    print(output_json)

    return jsonify(output_json)

@app.route('/addTag',methods=['POST'])
def addTag():   
    output_json = {}
    # check if the post request has the file part
    if 'file' not in request.files:
        output = {"message":"FILE NOT FOUND"}      
        return jsonify(output)
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        output = {"message":"FILE IS EMPTY"}  
        return jsonify(output)
    if file and allowed_file(file.filename): 
        output = {"message":"FILE UPLOADED SUCESSFULLY"}
        




if __name__ == "__main__":
    #face_load.load_known_faces()
    app.run(port=5001)