import os

from flask import Flask
from websocket import handle_websocket

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.debug = True

import views

def pydraw(env, start_response):  
    path = env["PATH_INFO"]  
    if path == "/":  
        return app(env, start_response)  
    elif path == "/websocket":  
        handle_websocket(env["wsgi.websocket"])   
    else:  
        return app(env, start_response)