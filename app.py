from flask import Flask, redirect, render_template, request, session, url_for, abort
from sqlalchemy import text
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)