#!/home/venv/bin/python
from flup.server.fcgi import WSGIServer
from flat import app

if __name__ == '__main__':
    WSGIServer(app).run()
