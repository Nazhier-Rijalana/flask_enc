from flask import Flask, redirect, url_for, render_template, request, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
import random
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Nani Koreeee???'
app.config['DEBUG'] = False
Bootstrap(app)

class Enc(FlaskForm):
    PlainText = StringField('PlainText', validators=[DataRequired()])
    key = StringField('Key : ', validators=[DataRequired()])
    secondKey = IntegerField('Second Key:', validators=[DataRequired()])

class Enc(FlaskForm):
    ChiperText = StringField('ChiperText', validators=[DataRequired()])
    key = StringField('Key : ', validators=[DataRequired()])
    secondKey = IntegerField('Second Key:', validators=[DataRequired()])

@app.route("/")
def index():
    return "Hello world"


@app.route("/home/encrypt", methods=['GET','POST'])
def encrypt():
    form = Enc()
    test = []
    ky = []
    ky2 = []
    if request.method == "POST":
        plaintext = form.PlainText.data
        kunci = form.key.data
        kunci2 = form.key2.data
        for i in range(len(plaintext)):
            if i % 2 == 0:
                if 65 <= ord(plaintext[i]) <= 90:
                    test.append(chr((ord(plaintext[i]) + 14) % 65 % 26 + 65))
                elif 97 <= ord(plaintext[i]) <= 122:
                    test.append(chr((ord(plaintext[i]) + 14) % 97 % 26 + 97))
                elif 48 <= ord(plaintext[i]) <= 57:
                    test.append(chr((ord(plaintext[i]) + 14) % 48 % 10 + 48))
                else:
                    test.append(plaintext[i])
                # test.append(chr((ord(plaintext[i]) + 13) % 65 % 26 + 65))
            elif i % 5 == 0:
                if 65 <= ord(plaintext[i]) <= 90:
                    test.append(chr((ord(plaintext[i]) + 17) % 65 % 26 + 65))
                elif 97 <= ord(plaintext[i]) <= 122:
                    test.append(chr((ord(plaintext[i]) + 17) % 97 % 26 + 97))
                elif 48 <= ord(plaintext[i]) <= 57:
                    test.append(chr((ord(plaintext[i]) + 17) % 48 % 10 + 48))
                else:
                    test.append(plaintext[i])
            elif i % 3 == 0:
                if 65 <= ord(plaintext[i]) <= 90:
                    test.append(chr((ord(plaintext[i]) + 24) % 65 % 26 + 65))
                elif 97 <= ord(plaintext[i]) <= 122:
                    test.append(chr((ord(plaintext[i]) + 24) % 97 % 26 + 97))
                elif 48 <= ord(plaintext[i]) <= 57:
                        test.append(chr((ord(plaintext[i]) + 24) % 48 % 7 + 48))
                else:
                    test.append(plaintext[i])
            else:
                if 65 <= ord(plaintext[i]) <= 90:
                    test.append(chr((ord(plaintext[i]) + 13) % 65 % 26 + 65))
                elif 97 <= ord(plaintext[i]) <= 122:
                    test.append(chr((ord(plaintext[i]) + 13) % 97 % 26 + 97))
                elif 48 <= ord(plaintext[i]) <= 57:
                    test.append(chr((ord(plaintext[i]) + 13) % 48 % 10 + 48))
                else:
                    test.append(plaintext[i])
        for i in range(len(key)):
            if i % 2 == 0:
                if 65 <= ord(key[i]) <= 90:
                    ky.append(chr((ord(key[i]) + 14) % 65 % 26 + 65))
                elif 97 <= ord(key[i]) <= 122:
                    ky.append(chr((ord(key[i]) + 14) % 97 % 26 + 97))
                elif 48 <= ord(key[i]) <= 57:
                    ky.append(chr((ord(key[i]) + 14) % 48 % 10 + 48))
                else:
                    ky.append(key[i])
                # ky.append(chr((ord(plaintext[i]) + 13) % 65 % 26 + 65))
            elif i % 5 == 0:
                if 65 <= ord(key[i]) <= 90:
                    ky.append(chr((ord(key[i]) + 17) % 65 % 26 + 65))
                elif 97 <= ord(key[i]) <= 122:
                    ky.append(chr((ord(key[i]) + 17) % 97 % 26 + 97))
                elif 48 <= ord(key[i]) <= 57:
                    ky.append(chr((ord(key[i]) + 17) % 48 % 10 + 48))
                else:
                    ky.append(key[i])
            elif i % 3 == 0:
                if 65 <= ord(key[i]) <= 90:
                    ky.append(chr((ord(key[i]) + 24) % 65 % 26 + 65))
                elif 97 <= ord(key[i]) <= 122:
                    ky.append(chr((ord(key[i]) + 24) % 97 % 26 + 97))
                elif 48 <= ord(key[i]) <= 57:
                        ky.append(chr((ord(key[i]) + 24) % 48 % 7 + 48))
                else:
                    ky.append(key[i])
            else:
                if 65 <= ord(key[i]) <= 90:
                    ky.append(chr((ord(key[i]) + 13) % 65 % 26 + 65))
                elif 97 <= ord(key[i]) <= 122:
                    ky.append(chr((ord(key[i]) + 13) % 97 % 26 + 97))
                elif 48 <= ord(key[i]) <= 57:
                    ky.append(chr((ord(key[i]) + 13) % 48 % 10 + 48))
                else:
                    ky.append(key[i])

        for i in range(len(key2)):
            if i % 2 == 0:
                if 65 <= ord(key2[i]) <= 90:
                    ky2.append(chr((ord(key2[i]) + 14) % 65 % 26 + 65))
                elif 97 <= ord(key2[i]) <= 122:
                    ky2.append(chr((ord(key2[i]) + 14) % 97 % 26 + 97))
                elif 48 <= ord(key2[i]) <= 57:
                    ky2.append(chr((ord(key2[i]) + 14) % 48 % 10 + 48))
                else:
                    ky2.append(key2[i])
                # ky2.append(chr((ord(plaintext[i]) + 13) % 65 % 26 + 65))
            elif i % 5 == 0:
                if 65 <= ord(key2[i]) <= 90:
                    ky2.append(chr((ord(key2[i]) + 17) % 65 % 26 + 65))
                elif 97 <= ord(key2[i]) <= 122:
                    ky2.append(chr((ord(key2[i]) + 17) % 97 % 26 + 97))
                elif 48 <= ord(key2[i]) <= 57:
                    ky2.append(chr((ord(key2[i]) + 17) % 48 % 10 + 48))
                else:
                    ky2.append(key2[i])
            elif i % 3 == 0:
                if 65 <= ord(key2[i]) <= 90:
                    ky2.append(chr((ord(key2[i]) + 24) % 65 % 26 + 65))
                elif 97 <= ord(key2[i]) <= 122:
                    ky2.append(chr((ord(key2[i]) + 24) % 97 % 26 + 97))
                elif 48 <= ord(key2[i]) <= 57:
                    ky2.append(chr((ord(key2[i]) + 24) % 48 % 7 + 48))
                else:
                    ky2.append(key2[i])
            else:
                if 65 <= ord(key2[i]) <= 90:
                    ky2.append(chr((ord(key2[i]) + 13) % 65 % 26 + 65))
                elif 97 <= ord(key2[i]) <= 122:
                    ky2.append(chr((ord(key2[i]) + 13) % 97 % 26 + 97))
                elif 48 <= ord(key2[i]) <= 57:
                    ky2.append(chr((ord(key2[i]) + 13) % 48 % 10 + 48))
                else:
                    ky2.append(key2[i])
        chiper_mentah = ''.join(test)
        kunci1_mentah = ''.join(ky)
        kunci2_mentah = ''.join(ky2)
        for i in range(len(chiper_mentah)):
            pass
    return render_template('encrypt.html', form=form)

def vinegereEnc(plaintext,chiper1,chiper2):
    alphabesar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphakecil = "abcdefghijklmnopqrstuvwxyz"
    angka = "1234567890"
    c = ""
    chipertext =[]
    kunci1 = []
    kunci2 = []
    for p in range(len(plaintext)):
        if 65 <= ord(plaintext[p]) <= 90:
            chipertext.append(alphabesar.find(plaintext[p]))
        elif 97 <= ord(plaintext[p]) <= 122:
            chipertext.append(alphakecil.find(plaintext[p]))
        elif 48 <= ord(plaintext[p]) <= 57:
            chipertext.append(angka.find(plaintext[p]))
        else:
            chipertext.append(plaintext[p])
    for k in range(len(chiper1)):
        if 65 <= ord(chiper1[p]) <= 90:
            kunci1.append(alphabesar.find(chiper1[p]))
        elif 97 <= ord(chiper1[p]) <= 122:
            kunci1.append(alphakecil.find(chiper1[p]))
        elif 48 <= ord(chiper1[p]) <= 57:
            kunci1.append(angka.find(chiper1[p]))
        else:
            kunci1.append(chiper1[p])
    for k in range(len(chiper2)):
        if 65 <= ord(chiper2[p]) <= 90:
            kunci2.append(alphabesar.find(chiper2[p]))
        elif 97 <= ord(chiper2[p]) <= 122:
            kunci2.append(alphakecil.find(chiper2[p]))
        elif 48 <= ord(chiper2[p]) <= 57:
            kunci2.append(angka.find(chiper2[p]))
        else:
            kunci2.append(chiper[p])
    


@app.route("/home/decrypt", methods=['GET','POST'])
def decrypt():
    pass



if __name__ == "__main__":
    app.run(host="0.0.0.0")
