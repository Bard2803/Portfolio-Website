from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import Cipher.Cipher as cr

### TO RUN FLASK
### python -m flask run 

# Confugre the application
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cipher", methods=['GET', 'POST'])
def cipher():
    ''' Cipher project'''

    if request.method == "GET":
        return render_template("cipher.html")
    else:
        # Get the message as str from cipher.html
        message = request.form.get("encrypted_message")

        # Get the shift as int from ciper.html
        shift = int(request.form.get("shift"))

        # Use the encryption from Cipher file 
        encrypted_message = cr.PlaintextMessage(message, shift).get_message_text_encrypted()

        return render_template("cipher.html", encrypted_message=encrypted_message)
