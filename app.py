from flask import Flask, render_template
import logging

logging.basicConfig(filename="/home/resume_logs.txt",format='%(asctime)s %(message)s',filemode='a')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def home():
    logger.debug("Home")
    return render_template('index.html')

@app.route('/resume')
def resume():
    logger.debug("Resume")
    return render_template('PRIYANK_Resume_EX.html')

@app.route('/projects')
def projects():
    logger.debug("At Projects")
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
