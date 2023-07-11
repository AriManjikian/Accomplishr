from flask import Flask, render_template, request
import pyrebase

config = {
  "apiKey": "AIzaSyB_4HVA1MMQWi56kUgrzwtsTrBh0itSa3o",
  "authDomain": "accomplishr-78ffd.firebaseapp.com",
  "projectId": "accomplishr-78ffd",
  "storageBucket": "accomplishr-78ffd.appspot.com",
  "messagingSenderId": "239633891989",
  "appId": "1:239633891989:web:134eb1151d741675c7d19c",
  "measurementId": "G-7QHRM0CMR6",
  "databaseURL": "https://accomplishr-78ffd-default-rtdb.firebaseio.com/"
}

app = Flask(__name__)

firebaseApp = pyrebase.initialize_app(config)
database = firebaseApp.database()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)