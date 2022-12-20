To create a flask app: 

1. Create a directory for your new application.
2. cd into the new directory
3. Open the project folder in vscode
4. Create a project environment
    a. On MacOS or Linux
        1. If needed on linux, type: sudo apt-get install python3-venv
        2. type: python3 -m venv env
        3. type: source env/bin/activate
    b. On Windows
        1. py -3 -m venv env
        2. env\scripts\activate
5. upgarde pip in the virtual environment
    a. Type: python -m pip install --upgrade pip
6. install flask into the venv
    a. Type: python -m pip install flask
7. Create app.py 
    a.  from flask import Flask
        app = Flask(__name__)

        @app.route("/")
        def home():
            return "Hello, Flask!"

        if __name__ == "__main__":
            app.run()
8. In the terminal type python3 app.py to get it to start.

Resources:
- https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application
- https://code.visualstudio.com/docs/python/tutorial-flask