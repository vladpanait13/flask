from flask import Flask, request, render_template
import docker 

app = Flask(__name__)
client = docker.from_env()

@app.route('/', methods=['GET', 'POST'])
def base_page():
    if request.method == 'POST':
        docker_image = request.form['docker_image']
        command = request.form['command']
        client.containers.run(docker_image, command)

        return render_template("my_docker.html")
    return render_template("my_docker.html")