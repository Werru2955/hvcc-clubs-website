from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/home/<page>")
def hello_world(page=None):
    return render_template('home.html', title=page)
