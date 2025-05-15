from flask import Flask, jsonify, requests
from config import app                

if __name__ == '__name__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )