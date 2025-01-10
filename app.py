from flask import Flask, request, render_template, jsonify

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

# @app.route('/guide', methods=['GET', 'POST'])
# def add_guide():
#   title = request.form['title']
#   return "<p>This is a POST request</p>"

@app.route('/hero', methods=['GET', 'POST'])
def hero():
    return render_template("index.html")

@app.route("/get-user/<user_id>") #example /get-user/12?extra="salve" 
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods = ["POST"])
def create_user():

    data = request.get_json()

    return jsonify(data), 201



#if __name__ == "__main__":
#    app.run()
