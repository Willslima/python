from flask import Flask
#pip Package installer for Python

app = Flask()

@app.route('/')
def index():
    return '<h1>Flask configutared</h1>'