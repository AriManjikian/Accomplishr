from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, db, auth


#firebase config
config = {
 "apiKey": "AIzaSyB_4HVA1MMQWi56kUgrzwtsTrBh0itSa3o",
  "authDomain": "accomplishr-78ffd.firebaseapp.com",
  "databaseURL": "https://accomplishr-78ffd-default-rtdb.firebaseio.com",
  "projectId": "accomplishr-78ffd",
  "storageBucket": "accomplishr-78ffd.appspot.com",
  "messagingSenderId": "239633891989",
  "appId": "1:239633891989:web:134eb1151d741675c7d19c",
  "measurementId": "G-7QHRM0CMR6"
}

app = Flask(__name__)

#FIREBASE
cred = credentials.Certificate("credentials.json")
firebaseApp = firebase_admin.initialize_app(cred, {"databaseURL": "https://accomplishr-78ffd-default-rtdb.firebaseio.com/"})
ref = db.reference('/Users')
ref.push({'name':'boghos', 'email': 'bkaradanayan@blig.com'})


#FLASK
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        
        if password == confirm:
            ref = db.reference('/Users')
            ref.push({'name':'boghos', 'email': 'bkaradanayan@blig.com'})
            print('rigev')
        return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    