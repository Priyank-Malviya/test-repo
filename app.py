from flask import Flask, render_template
import os 
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    print("At home")
    os.system("echo 'at_home'")
    return render_template('index.html')

@app.route('/resume')
def resume():
    print("Resume")
    return render_template('PRIYANK_Resume_EX.html')

@app.route('/projects')
def projects():
    print("At Projects")
    return render_template('projects.html')

@app.route('/path')
def path():
    dir_path = str(os.path.dirname(os.path.realpath(__file__)))
    print("At Path")
    return render_template('path.html',path=dir_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
