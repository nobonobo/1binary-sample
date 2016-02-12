import os
import sys

from gevent import pywsgi

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
from app.wsgi import application


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    addr = ('', 8080)
    server = pywsgi.WSGIServer(addr, application)
    print('listener:', addr)
    server.serve_forever()

if __name__ == "__main__":
    main()
