#!/usr/bin/env python
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from app import plydraw

if __name__ == '__main__':
    http_server = WSGIServer(('',5000), my_app, handler_class=WebSocketHandler)
    http_server.serve_forever()