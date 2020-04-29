from flask import Flask, render_template, request, session, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from analysis import Distance

from flask_dropzone import Dropzone
from flask_sqlalchemy import SQLAlchemy

# Load Model Class
from turi_model import TuriObj
from db_model import DBObj
import pandas as pd
import sqlite3

# db Config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///model/mark.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'mark'

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/static/assets/file-upload'

# Activate app
dropzone = Dropzone(app)
db = SQLAlchemy(app)


# Connect Upload Router
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

a = TuriObj()
b = Distance()
sql_obj = DBObj()


@app.route('/')
def hello_world():
    return render_template('basic.html', sql_obj= sql_obj.obj_list, Distance = b)


@app.route('/test', methods=['POST', 'GET'])
def upload():
    print('test start')
    if "file_urls" not in session:
        session['file_urls'] = "../../static/assets/img/samsung.jpg"
    # list to hold our uploaded image urls
    file_urls = session['file_urls']

    # handle image upload from Dropszone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)

            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename
            )

            # append image urls
            file_urls = photos.url(filename)

        session['file_urls'] = file_urls
        print('uploding')
        return "uploading..."
    # return dropzone template on GET request
    print('test end2')
    return 'good'


@app.route('/results')
def results():
    # set the file_urls and remove the session variable
    file_url = session['file_urls']
    a.create_sample(file_url)
    a.create_list()
    return render_template('basic.html', file_url=file_url, Distance = b)


@app.route('/start')
def start():
    sql_obj.open("model/mark.db")
    b.set_graph()
    sql_obj.obj_list = []
    for i in a.pathlist:
        sql_obj.obj_list.append(sql_obj.find(i))
    return render_template('basic.html', file_url=session['file_urls'], Distance= b, sql_obj=sql_obj.obj_list, turi = a.distance_list)


if __name__ == '__main__':
    app.run()
