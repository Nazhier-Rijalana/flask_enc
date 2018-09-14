from flask import Flask, redirect, url_for, render_template, request, flash, request, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
import random
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired, Email, Length, NumberRange
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Nani Koreeee???'
app.config['DEBUG'] = False
Bootstrap(app)

class Enc(FlaskForm):
    PlainText = TextAreaField('PlainText', validators=[DataRequired()])
    key = StringField('Key : ', validators=[DataRequired()])
    secondKey = IntegerField('Second Key:', validators=[DataRequired(), NumberRange(min=0,max=11)])
    submit = SubmitField("Submit ")

class Dec(FlaskForm):
    ChiperText = TextAreaField('ChiperText', validators=[DataRequired()])
    key = StringField('Key : ', validators=[DataRequired()])
    secondKey = IntegerField('Second Key:', validators=[DataRequired(), NumberRange(min=0,max=11)])
    submit = SubmitField("Submit ")
@app.route("/")
def index():
    return redirect(url_for('encrypt'))
@app.route("/home/encrypt")
def enc():
    form = Enc()
    return render_template('encrypt.html',form=form)

@app.route("/home/encrypt/proccess", methods=['GET','POST'])
def encrypt():
    form = Enc()
    test = []
    ky = []
    ky2 = 0
    response = ""
    if request.method == "POST":
        plaintext = form.PlainText.data
        key = form.key.data
        key2 = form.secondKey.data
        for i in range(len(plaintext)):
            if i % 2 == 0:
                if 65 <= ord(plaintext[i]) <= 90:
                    test.append(chr((ord(plaintext[i]) + 14) % 65 % 26 + 65))
                elif 97 <= ord(plaintext[i]) <= 122:
                    test.append(chr((ord(plaintext[i]) + 14) % 97 % 26 + 97))
                elif 48 <= ord(plaintext[i]) <= 57:
                    test.append(chr((ord(plaintext[i]) + 14) % 48 % 10 + 48))
                elif 32 <= ord(plaintext[i]) <= 47:
                    test.append(chr((ord(plaintext[i]) + 14) % 32 % 15 + 32))
                elif 58 <= ord(plaintext[i]) <= 64:
                    test.append(chr((ord(plaintext[i]) + 14) % 58 % 6 + 58))
                elif 91 <= ord(plaintext[i]) <= 96:
                    test.append(chr((ord(plaintext[i]) + 14) % 91 % 5 + 91))
                elif 123 <= ord(plaintext[i]) <= 126:
                    test.append(chr((ord(plaintext[i]) + 14) % 123 % 3 + 123))
                else:
                    test.append(plaintext[i])
            elif i % 5 == 0:
                if 65 <= ord(plaintext[i]) <= 90:
                    test.append(chr((ord(plaintext[i]) + 17) % 65 % 26 + 65))
                elif 97 <= ord(plaintext[i]) <= 122:
                    test.append(chr((ord(plaintext[i]) + 17) % 97 % 26 + 97))
                elif 48 <= ord(plaintext[i]) <= 57:
                    test.append(chr((ord(plaintext[i]) + 17) % 48 % 10 + 48))
                elif 32 <= ord(plaintext[i]) <= 47:
                    test.append(chr((ord(plaintext[i]) + 17) % 32 % 15 + 32))
                elif 58 <= ord(plaintext[i]) <= 64:
                    test.append(chr((ord(plaintext[i]) + 17) % 58 % 6 + 58))
                elif 91 <= ord(plaintext[i]) <= 96:
                    test.append(chr((ord(plaintext[i]) + 17) % 91 % 5 + 91))
                elif 123 <= ord(plaintext[i]) <= 126:
                    test.append(chr((ord(plaintext[i]) + 17) % 123 % 3 + 123))
                else:
                    test.append(plaintext[i])
            elif i % 3 == 0:
                if 65 <= ord(plaintext[i]) <= 90:
                    test.append(chr((ord(plaintext[i]) + 24) % 65 % 26 + 65))
                elif 97 <= ord(plaintext[i]) <= 122:
                    test.append(chr((ord(plaintext[i]) + 24) % 97 % 26 + 97))
                elif 48 <= ord(plaintext[i]) <= 57:
                    test.append(chr((ord(plaintext[i]) + 24) % 48 % 7 + 48))
                elif 32 <= ord(plaintext[i]) <= 47:
                    test.append(chr((ord(plaintext[i]) + 24) % 32 % 15 + 32))
                elif 58 <= ord(plaintext[i]) <= 64:
                    test.append(chr((ord(plaintext[i]) + 24) % 58 % 6 + 58))
                elif 91 <= ord(plaintext[i]) <= 96:
                    test.append(chr((ord(plaintext[i]) + 24) % 91 % 5 + 91))
                elif 123 <= ord(plaintext[i]) <= 126:
                    test.append(chr((ord(plaintext[i]) + 24) % 123 % 3 + 123))
                else:
                    test.append(plaintext[i])
            else:
                if 65 <= ord(plaintext[i]) <= 90:
                    test.append(chr((ord(plaintext[i]) + 13) % 65 % 26 + 65))
                elif 97 <= ord(plaintext[i]) <= 122:
                    test.append(chr((ord(plaintext[i]) + 13) % 97 % 26 + 97))
                elif 48 <= ord(plaintext[i]) <= 57:
                    test.append(chr((ord(plaintext[i]) + 13) % 48 % 10 + 48))
                elif 32 <= ord(plaintext[i]) <= 47:
                    test.append(chr((ord(plaintext[i]) + 13) % 32 % 15 + 32))
                elif 58 <= ord(plaintext[i]) <= 64:
                    test.append(chr((ord(plaintext[i]) + 13) % 58 % 6 + 58))
                elif 91 <= ord(plaintext[i]) <= 96:
                    test.append(chr((ord(plaintext[i]) + 13) % 91 % 5 + 91))
                elif 123 <= ord(plaintext[i]) <= 126:
                    test.append(chr((ord(plaintext[i]) + 13) % 123 % 3 + 123))
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
                elif 32 <= ord(key[i]) <= 47:
                    ky.append(chr((ord(key[i]) + 14) % 32 % 15 + 32))
                elif 58 <= ord(key[i]) <= 64:
                    ky.append(chr((ord(key[i]) + 14) % 58 % 6 + 58))
                elif 91 <= ord(key[i]) <= 96:
                    ky.append(chr((ord(key[i]) + 14) % 91 % 5 + 91))
                elif 123 <= ord(key[i]) <= 126:
                    ky.append(chr((ord(key[i]) + 14) % 123 % 3 + 123))
                else:
                    ky.append(key[i])
            elif i % 5 == 0:
                if 65 <= ord(key[i]) <= 90:
                    ky.append(chr((ord(key[i]) + 17) % 65 % 26 + 65))
                elif 97 <= ord(key[i]) <= 122:
                    ky.append(chr((ord(key[i]) + 17) % 97 % 26 + 97))
                elif 48 <= ord(key[i]) <= 57:
                    ky.append(chr((ord(key[i]) + 17) % 48 % 10 + 48))
                elif 32 <= ord(key[i]) <= 47:
                    ky.append(chr((ord(key[i]) + 17) % 32 % 15 + 32))
                elif 58 <= ord(key[i]) <= 64:
                    ky.append(chr((ord(key[i]) + 17) % 58 % 6 + 58))
                elif 91 <= ord(key[i]) <= 96:
                    ky.append(chr((ord(key[i]) + 17) % 91 % 5 + 91))
                elif 123 <= ord(key[i]) <= 126:
                    ky.append(chr((ord(key[i]) + 17) % 123 % 3 + 123))
                else:
                    ky.append(key[i])
            elif i % 3 == 0:
                if 65 <= ord(key[i]) <= 90:
                    ky.append(chr((ord(key[i]) + 24) % 65 % 26 + 65))
                elif 97 <= ord(key[i]) <= 122:
                    ky.append(chr((ord(key[i]) + 24) % 97 % 26 + 97))
                elif 48 <= ord(key[i]) <= 57:
                    ky.append(chr((ord(key[i]) + 24) % 48 % 7 + 48))
                elif 32 <= ord(key[i]) <= 47:
                    ky.append(chr((ord(key[i]) + 24) % 32 % 15 + 32))
                elif 58 <= ord(key[i]) <= 64:
                    ky.append(chr((ord(key[i]) + 24) % 58 % 6 + 58))
                elif 91 <= ord(key[i]) <= 96:
                    ky.append(chr((ord(key[i]) + 24) % 91 % 5 + 91))
                elif 123 <= ord(key[i]) <= 126:
                    ky.append(chr((ord(key[i]) + 24) % 123 % 3 + 123))
                else:
                    ky.append(key[i])
            else:
                if 65 <= ord(key[i]) <= 90:
                    ky.append(chr((ord(key[i]) + 13) % 65 % 26 + 65))
                elif 97 <= ord(key[i]) <= 122:
                    ky.append(chr((ord(key[i]) + 13) % 97 % 26 + 97))
                elif 48 <= ord(key[i]) <= 57:
                    ky.append(chr((ord(key[i]) + 13) % 48 % 10 + 48))
                elif 32 <= ord(key[i]) <= 47:
                    ky.append(chr((ord(key[i]) + 13) % 32 % 15 + 32))
                elif 58 <= ord(key[i]) <= 64:
                    ky.append(chr((ord(key[i]) + 13) % 58 % 6 + 58))
                elif 91 <= ord(key[i]) <= 96:
                    ky.append(chr((ord(key[i]) + 13) % 91 % 5 + 91))
                elif 123 <= ord(key[i]) <= 126:
                    ky.append(chr((ord(key[i]) + 13) % 123 % 3 + 123))
                else:
                    ky.append(key[i])
        chiper_mentah = ''.join(test)
        kunci1_mentah = ''.join(ky)
        kunci2_mentah = key2
        print chiper_mentah
        print kunci1_mentah
        print kunci2_mentah
        fin = CustomEnc(chiper_mentah,kunci1_mentah)
        final = RotGet(fin,kunci2_mentah)
        response = make_response(json.dumps(final))
        response.content_type = 'application/json'
    return response

def CustomEnc(plaintext,chiper1):
    universe = [c for c in (chr(i) for i in range(32,127))]
    uni_len = len(universe)
    k_len = len(chiper1)
    ret_plain= ""
    for i,l in enumerate(plaintext):
        if l not in universe:
            ret_plain += 1
        else:
            plain_index = universe.index(l)
            k = chiper1[i % k_len]
            key_index = universe.index(k)
            code = universe[(plain_index+key_index)%uni_len]
            ret_plain += code
    # test = RotGet(ret_plain,chiper2)
    return ret_plain
    # response = make_response(test)
    # respose.content_type = 'application/json'
    # return respose

def RotGet(final,key2):
    ky = []
    for i in range(len(final)):
        if 65 <= ord(final[i]) <= 90:
            ky.append(chr((ord(final[i]) + key2) % 65 % 26 + 65))
        elif 97 <= ord(final[i]) <= 122:
            ky.append(chr((ord(final[i]) + key2) % 97 % 26 + 97))
        elif 48 <= ord(final[i]) <= 57:
            ky.append(chr((ord(final[i]) + key2) % 48 % 10 + 48))
        elif 32 <= ord(final[i]) <= 47:
            ky.append(chr((ord(final[i]) + key2) % 32 % 15 + 32))
        elif 58 <= ord(final[i]) <= 64:
            ky.append(chr((ord(final[i]) + key2) % 58 % 6 + 58))
        elif 91 <= ord(final[i]) <= 96:
            ky.append(chr((ord(final[i]) + key2) % 91 % 5 + 91))
        elif 123 <= ord(final[i]) <= 126:
            ky.append(chr((ord(final[i]) + key2) % 123 % 3 + 123))
        else:
            ky.append(final[i])
    return ''.join(ky)


@app.route("/home/hint")
def Hint():
    form = Dec()
    return render_template('hint.html', form=form)

@app.route("/home/decrypt/proccess", methods=['GET','POST'])
def decrypt():
    form = Dec()
    test = []
    ky = []
    ky2 = []
    response = ""
    if request.method == "POST":
        mentah = form.ChiperText.data
        key1 = form.key.data
        secKey = form.secondKey.data
        kunci2_mentah = secKey
        hasil = RotrevGet(mentah,kunci2_mentah)
        for i in range(len(key1)):
            if i % 2 == 0:
                if 65 <= ord(key1[i]) <= 90:
                    ky.append(chr((ord(key1[i]) % 65 + 14) % 26 + 65))
                elif 97 <= ord(key1[i]) <= 122:
                    ky.append(chr((ord(key1[i]) % 97 + 14) % 26 + 97))
                elif 48 <= ord(key1[i]) <= 57:
                    ky.append(chr((ord(key1[i]) % 48 + 14) % 10 + 48))
                elif 32 <= ord(key1[i]) <= 47:
                    ky.append(chr((ord(key1[i]) % 32 + 14) % 15 + 32))
                elif 58 <= ord(key1[i]) <= 64:
                    ky.append(chr((ord(key1[i]) % 58 + 14) % 6 + 58))
                elif 91 <= ord(key1[i]) <= 96:
                    ky.append(chr((ord(key1[i]) % 91 + 14) % 5 + 91))
                elif 123 <= ord(key1[i]) <= 126:
                    ky.append(chr((ord(key1[i]) % 123 + 14) % 3 + 123))
                else:
                    ky.append(key1[i])
            elif i % 5 == 0:
                if 65 <= ord(key1[i]) <= 90:
                    ky.append(chr((ord(key1[i]) % 65 + 17) % 26 + 65))
                elif 97 <= ord(key1[i]) <= 122:
                    ky.append(chr((ord(key1[i]) % 97 + 17) % 26 + 97))
                elif 48 <= ord(key1[i]) <= 57:
                    ky.append(chr((ord(key1[i]) % 48 + 17) % 10 + 48))
                elif 32 <= ord(key1[i]) <= 47:
                    ky.append(chr((ord(key1[i]) % 32 + 17)% 15 + 32))
                elif 58 <= ord(key1[i]) <= 64:
                    ky.append(chr((ord(key1[i]) % 58 + 17)% 6 + 58))
                elif 91 <= ord(key1[i]) <= 96:
                    ky.append(chr((ord(key1[i]) % 91  + 17)% 5 + 91))
                elif 123 <= ord(key1[i]) <= 126:
                    ky.append(chr((ord(key1[i]) % 123 +  17)% 3 + 123))
                else:
                    ky.append(key1[i])
            elif i % 3 == 0:
                if 65 <= ord(key1[i]) <= 90:
                    ky.append(chr((ord(key1[i]) % 65  + 24)% 26 + 65))
                elif 97 <= ord(key1[i]) <= 122:
                    ky.append(chr((ord(key1[i]) % 97  + 24)% 26 + 97))
                elif 48 <= ord(key1[i]) <= 57:
                    ky.append(chr((ord(key1[i]) % 48  + 24)% 7 + 48))
                elif 32 <= ord(key1[i]) <= 47:
                    ky.append(chr((ord(key1[i]) % 32  + 24)% 15 + 32))
                elif 58 <= ord(key1[i]) <= 64:
                    ky.append(chr((ord(key1[i]) % 58  + 24)% 6 + 58))
                elif 91 <= ord(key1[i]) <= 96:
                    ky.append(chr((ord(key1[i]) % 91 + 24) % 5 + 91))
                elif 123 <= ord(key1[i]) <= 126:
                    ky.append(chr((ord(key1[i]) % 123 + 24) % 3 + 123))
                else:
                    ky.append(key1[i])
            else:
                if 65 <= ord(key1[i]) <= 90:
                    ky.append(chr((ord(key1[i]) % 65  + 13)% 26 + 65))
                elif 97 <= ord(key1[i]) <= 122:
                    ky.append(chr((ord(key1[i]) % 97 + 13) % 26 + 97))
                elif 48 <= ord(key1[i]) <= 57:
                    ky.append(chr((ord(key1[i]) % 48 + 13) % 10 + 48))
                elif 32 <= ord(key1[i]) <= 47:
                    ky.append(chr((ord(key1[i]) % 32 + 13) % 15 + 32))
                elif 58 <= ord(key1[i]) <= 64:
                    ky.append(chr((ord(key1[i]) % 58 + 13) % 6 + 58))
                elif 91 <= ord(key1[i]) <= 96:
                    ky.append(chr((ord(key1[i]) % 91 + 13) % 5 + 91))
                elif 123 <= ord(key1[i]) <= 126:
                    ky.append(chr((ord(key1[i]) % 123 + 13) % 3 + 123))
                else:
                    ky.append(key1[i])
        kunci1_mentah = ''.join(ky)
        chipertext = DecCustomEnc(hasil,kunci1_mentah)
        for i in range(len(chipertext)):
            if i % 2 == 0:
                if 65 <= ord(chipertext[i]) <= 90:
                    test.append(chr((ord(chipertext[i]) % 65 - 14) % 26 + 65))
                elif 97 <= ord(chipertext[i]) <= 122:
                    test.append(chr((ord(chipertext[i])% 97 - 14)  % 26 + 97))
                elif 48 <= ord(chipertext[i]) <= 57:
                    test.append(chr((ord(chipertext[i])% 48 - 14)  % 10 + 48))
                elif 32 <= ord(chipertext[i]) <= 47:
                    test.append(chr((ord(chipertext[i])% 32 - 14)  % 15 + 32))
                elif 58 <= ord(chipertext[i]) <= 64:
                    test.append(chr((ord(chipertext[i])% 58 - 14)  % 6 + 58))
                elif 91 <= ord(chipertext[i]) <= 96:
                    test.append(chr((ord(chipertext[i])% 91 - 14)  % 5 + 91))
                elif 123 <= ord(chipertext[i]) <= 126:
                    test.append(chr((ord(chipertext[i])% 123 - 14)  % 3 + 123))
                else:
                    test.append(chipertext[i])
            elif i % 5 == 0:
                if 65 <= ord(chipertext[i]) <= 90:
                    test.append(chr((ord(chipertext[i]) % 65 - 17) % 26 + 65))
                elif 97 <= ord(chipertext[i]) <= 122:
                    test.append(chr((ord(chipertext[i]) % 97 - 17) % 26 + 97))
                elif 48 <= ord(chipertext[i]) <= 57:
                    test.append(chr((ord(chipertext[i]) % 48 - 17) % 10 + 48))
                elif 32 <= ord(chipertext[i]) <= 47:
                    test.append(chr((ord(chipertext[i]) % 32 - 17) % 15 + 32))
                elif 58 <= ord(chipertext[i]) <= 64:
                    test.append(chr((ord(chipertext[i]) % 58 - 17) % 6 + 58))
                elif 91 <= ord(chipertext[i]) <= 96:
                    test.append(chr((ord(chipertext[i]) % 91 - 17) % 5 + 91))
                elif 123 <= ord(chipertext[i]) <= 126:
                    test.append(chr((ord(chipertext[i]) % 123 - 17) % 3 + 123))
                else:
                    test.append(chipertext[i])
            elif i % 3 == 0:
                if 65 <= ord(chipertext[i]) <= 90:
                    test.append(chr((ord(chipertext[i]) % 65 - 24) % 26 + 65))
                elif 97 <= ord(chipertext[i]) <= 122:
                    test.append(chr((ord(chipertext[i]) % 97 - 24) % 26 + 97))
                elif 48 <= ord(chipertext[i]) <= 57:
                    test.append(chr((ord(chipertext[i]) % 48 - 24) % 7 + 48))
                elif 32 <= ord(chipertext[i]) <= 47:
                    test.append(chr((ord(chipertext[i]) % 32 - 24) % 15 + 32))
                elif 58 <= ord(chipertext[i]) <= 64:
                    test.append(chr((ord(chipertext[i]) % 58 - 24) % 6 + 58))
                elif 91 <= ord(chipertext[i]) <= 96:
                    test.append(chr((ord(chipertext[i]) % 91 - 24) % 5 + 91))
                elif 123 <= ord(chipertext[i]) <= 126:
                    test.append(chr((ord(chipertext[i]) % 123 - 24) % 3 + 123))
                else:
                    test.append(chipertext[i])
            else:
                if 65 <= ord(chipertext[i]) <= 90:
                    test.append(chr((ord(chipertext[i]) % 65 - 13) % 26 + 65))
                elif 97 <= ord(chipertext[i]) <= 122:
                    test.append(chr((ord(chipertext[i]) % 97 - 13) % 26 + 97))
                elif 48 <= ord(chipertext[i]) <= 57:
                    test.append(chr((ord(chipertext[i]) % 48 - 13) % 10 + 48))
                elif 32 <= ord(chipertext[i]) <= 47:
                    test.append(chr((ord(chipertext[i]) % 32 - 13) % 15 + 32))
                elif 58 <= ord(chipertext[i]) <= 64:
                    test.append(chr((ord(chipertext[i]) % 58 - 13) % 6 + 58))
                elif 91 <= ord(chipertext[i]) <= 96:
                    test.append(chr((ord(chipertext[i]) % 91 - 13) % 5 + 91))
                elif 123 <= ord(chipertext[i]) <= 126:
                    test.append(chr((ord(chipertext[i]) % 123 - 13) % 3 + 123))
                else:
                    test.append(chipertext[i])
        plain_matang = ''.join(test)
        response = make_response(json.dumps(plain_matang))
        response.content_type = 'application/json'
    return response

def RotrevGet(final,key2):
    ky = []
    for i in range(len(final)):
        if 65 <= ord(final[i]) <= 90:
            ky.append(chr((ord(final[i]) % 65 - key2) % 26 + 65))
        elif 97 <= ord(final[i]) <= 122:
            ky.append(chr((ord(final[i]) % 97 - key2)  % 26 + 97))
        elif 48 <= ord(final[i]) <= 57:
            ky.append(chr((ord(final[i]) % 48 - key2) % 10 + 48))
        elif 32 <= ord(final[i]) <= 47:
            ky.append(chr((ord(final[i]) % 32 - key2)  % 15 + 32))
        elif 58 <= ord(final[i]) <= 64:
            ky.append(chr((ord(final[i]) % 58 - key2) % 6 + 58))
        elif 91 <= ord(final[i]) <= 96:
            ky.append(chr((ord(final[i]) % 91 - key2) % 5 + 91))
        elif 123 <= ord(final[i]) <= 126:
            ky.append(chr((ord(final[i]) % 123 - key2) % 3 + 123))
        else:
            ky.append(final[i])
    return ''.join(ky)

def DecCustomEnc(chiper,key1):
    universe = [c for c in (chr(i) for i in range(32,127))]
    uni_len = len(universe)
    k_len = len(key1)
    # keygen = RotrevGet(chiper,key2)
    # print keygen
    ret_plain = ""
    for i,l in enumerate(chiper):
        if l not in universe:
            ret_plain += 1
        else:
            plain_index = universe.index(l)
            k = key1[i % k_len]
            key_index = universe.index(k)
            key_index *= -1
            code = universe[(plain_index+key_index)%uni_len]
            ret_plain += code
    return ret_plain

@app.route('/home/decrypt/', methods=['GET','POST'])
def dec():
    form = Dec()
    return render_template('decrypt.html',form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
