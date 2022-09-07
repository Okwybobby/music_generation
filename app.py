import flask
from flask import Flask, request, render_template
import json
#import main

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000, use_reloader=False)    
