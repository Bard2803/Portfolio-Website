from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# Confugre the application
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cipher", methods=['GET', 'POST'])
def cipher():
    ''' Cipher project'''

    return render_template("cipher.html")
