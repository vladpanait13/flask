from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "<p>Flask Project!</p>"


# The server will always send to us a GET, by default. To have a POST request,
# we have to send information or data to the server. We do this by 
# implementing a 'submit' or 'next' button, that will send data to the server

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_post()
    else:
        return login_get()

@app.get('/login')
def login_get():
    return "<p>Hello, world!<p>"

@app.post('/login')
def login_post():
    return "<p>Hello, world!</p>"




