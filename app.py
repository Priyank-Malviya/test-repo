from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    print("Home")
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('PRIYANK_Resume_EX.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run()
