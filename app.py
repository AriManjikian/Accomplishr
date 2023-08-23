from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, db, auth



app = Flask(__name__)


#FLASK
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/privacypolicy")
def privacypolicy():
    return render_template("privacypolicy.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    