from flask import Flask
from os import environ as env
from worker.utils import create_path

app = Flask(__name__)

try:
    SECRET = open("secret.txt", "r").read()
except:
    SECRET = env['SECRET']

app.config['SECRET'] = SECRET
app.config['MAX_CONTENT_LENGTH'] = 15 * 1024 * 1000 # limit the files size to 15 MB
app.config['UPLOAD_EXTENSIONS'] = ['.jpeg', '.jpg', '.png']
app.config['UPLOAD_PATH'] = 'temp'
create_path(app.config['UPLOAD_PATH'])


from app import views