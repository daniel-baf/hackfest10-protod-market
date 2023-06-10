from flask import Flask

app = Flask(__name__)

@app.route('/')
def start_method():  # put application's code here
    return 'main'