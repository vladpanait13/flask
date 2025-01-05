# Flask App

# Use GitHub cli

`git clone https://github.com/vladpanait13/flask.git`

`git remote set-url origin git@github.com:vladpanait13/flask.git`

`git status`

`git branch`

`git remote -v`

## git push

`git checkout -b "new_branch"`

`git add .`

`git commit -m "commit message"`

`git push origin main`

## git pull

`git checkout main`

`git pull origin main`

# Environment variables

It is recommended to set up environment variables in python (especially if working on many projects) in order to not mess up the python environment installed locally.

### CREATE AN ENVIRONMENT

A clone of your python interpreter in which you specify which packages you use. You do not install packages on your global interpreter, but on a local interpreter set up for each of your projects.

`mkdir myproject`

`cd myproject`

`py -3 -m venv .venv`

### ACTIVATE ENVIRONMENT

Before working on the project, activate the corresponding environment

`.venv\Scripts\activate`

### Install pylint

` $ pip install -U pylint`

### Install Flask

` $ pip install flask`

### Hide .venv folder

To hide the env folder, create a new file with the name ".gitignore". Add the following line of code:

`# Virtual Environment`
`.venv/ `

# Run the app

To run the app, type the followint in the terminal:

`python -m flask`
`flask run`

Because our file is named 'app.py', the command will look like this.
If our file was named 'hello.py', the command would be 'flask --app hello run'
