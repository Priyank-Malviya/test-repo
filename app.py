from flask import Flask, render_template
import logging
import os 

logging.basicConfig(filename="app/resume_logs.txt",format='%(asctime)s %(message)s',filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def home():
    logger.error("Home")
    return render_template('index.html')

@app.route('/resume')
def resume():
    logger.error("Resume")
    return render_template('PRIYANK_Resume_EX.html')

@app.route('/projects')
def projects():
    logger.error("At Projects")
    return render_template('projects.html')

@app.route('/path')
def path():
    dir_path = str(os.path.dirname(os.path.realpath(__file__)))
    logger.error("At Path")
    return render_template('path.html',path=dir_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
