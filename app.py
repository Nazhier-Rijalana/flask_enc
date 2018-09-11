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

class Dec(FlaskForm):
    ChiperText = StringField('ChiperText', validators=[DataRequired()])
    key = StringField('Key : ', validators=[DataRequired()])
    secondKey = IntegerField('Second Key:', validators=[DataRequired()])

@app.route("/home/encrypt")
def enc():
    form = Enc()
    return render_template('encrypt.html',form=form)

@app.route("/home/encrypt/proccess", methods=['GET','POST'])
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

        chiper_mentah = ''.join(test)
        kunci1_mentah = ''.join(ky)
        kunci2_mentah = ky2
        final = CustomEnc(chiper_mentah,kunci1_mentah,kunci2_mentah)
    return final

def CustomEnc(plaintext,chiper1,chiper2):
    alphabesar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphakecil = "abcdefghijklmnopqrstuvwxyz"
    angka = "1234567890"
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
        if 65 <= ord(chiper1[k]) <= 90:
            kunci1.append(alphabesar.find(chiper1[k]))
        elif 97 <= ord(chiper1[k]) <= 122:
            kunci1.append(alphakecil.find(chiper1[k]))
        elif 48 <= ord(chiper1[k]) <= 57:
            kunci1.append(angka.find(chiper1[k]))
        else:
            kunci1.append(chiper1[k])
    # for k in range(len(chiper2)):
    #     if 65 <= ord(chiper2[k]) <= 90:
    #         kunci2.append(alphabesar.find(chiper2[k]))
    #     elif 97 <= ord(chiper2[k]) <= 122:
    #         kunci2.append(alphakecil.find(chiper2[k]))
    #     elif 48 <= ord(chiper2[k]) <= 57:
    #         kunci2.append(angka.find(chiper2[k]))
    #     else:
    #         kunci2.append(chiper[k])
    final = []
    if len(plaintext) == len(chiper1):
        for l in range(len(plaintext)):
            if 65 <= ord(plaintext[p]) <= 90:
                final.append(chr(ord(plaintext[i]) + chiper2 + (ord(chiper1[l])%65) % 26 + 65))

                # es = alphabesar.find(plaintext[i] +  ))
                # chipertext.append(alphabesar.find(plaintext[p]))
            elif 97 <= ord(plaintext[p]) <= 122:
                final.append(chr(ord(plaintext[i]) + chiper2 + (ord(chiper1[l])%97)  % 26 + 97))
                # chipertext.append(alphakecil.find(plaintext[p]))
            elif 48 <= ord(plaintext[p]) <= 57:
                final.append(chr(ord(plaintext[i]) + chiper2 + (ord(chiper1[l])%48)  % 10 + 48 ))
                # chipertext.append(angka.find(plaintext[p]))
            else:
                final.append(chr(plaintext[i] + chiper2 + (ord(chiper1[l]))))
                # chipertext.append(plaintext[p])
    else:
        for i n range(len(plaintext)):
            for j in range(len(chiper1)):
                if 65 <= ord(plaintext[i]) <= 90:
                    final.append(chr(ord(plaintext[i]) + chiper2 + (ord(chiper1[j])% 65) %26 + 65))
                elif 97 <= ord(plaintext[i]) <= 122:
                    final.append(chr(ord(plaintext[i]) + chiper2 + (ord(chiper1[j])% 97) %26 + 65))
                elif 48 <= ord(plaintext[i]) <= 57:
                    final.append(chr(ord(plaintext[i]) + chiper2 + (ord(chiper[j])% 48) %26 + 10))
                else:
                    final.append(chr(ord(plaintext[i])+ chiper2 ))

    return ''.join(final)

@app.route("/home/hint")
def Hint():
    return render_template('hint.html')

@app.route("/home/decrypt", methods=['GET','POST'])
def decrypt():
    form = Dec()
    test = []
    ky = []
    ky2 = []
    hasil =""
    if request.method == "POST":
        chipertext = form.ChiperText.data
        key1 = form.key.data
        secKey = form.secondkey.data
        for i in range(len(chipertext)):
            if i % 2 == 0:
                if 65 <= ord(chipertext[i]) <= 90:
                    test.append(chr((ord(chipertext[i]) - 14) % 65 % 26 + 65))
                elif 97 <= ord(chipertext[i]) <= 122:
                    test.append(chr((ord(chipertext[i]) - 14) % 97 % 26 + 97))
                elif 48 <= ord(chipertext[i]) <= 57:
                    test.append(chr((ord(chipertext[i]) - 14) % 48 % 10 + 48))
                else:
                    test.append(chipertext[i])
                # test.append(chr((ord(chipertext[i]) + 13) % 65 % 26 + 65))
            elif i % 5 == 0:
                if 65 <= ord(chipertext[i]) <= 90:
                    test.append(chr((ord(chipertext[i]) - 17) % 65 % 26 + 65))
                elif 97 <= ord(chipertext[i]) <= 122:
                    test.append(chr((ord(chipertext[i]) - 17) % 97 % 26 + 97))
                elif 48 <= ord(chipertext[i]) <= 57:
                    test.append(chr((ord(chipertext[i]) - 17) % 48 % 10 + 48))
                else:
                    test.append(chipertext[i])
            elif i % 3 == 0:
                if 65 <= ord(chipertext[i]) <= 90:
                    test.append(chr((ord(chipertext[i]) - 24) % 65 % 26 + 65))
                elif 97 <= ord(chipertext[i]) <= 122:
                    test.append(chr((ord(chipertext[i]) - 24) % 97 % 26 + 97))
                elif 48 <= ord(chipertext[i]) <= 57:
                        test.append(chr((ord(chipertext[i]) - 24) % 48 % 7 + 48))
                else:
                    test.append(chipertext[i])
            else:
                if 65 <= ord(chipertext[i]) <= 90:
                    test.append(chr((ord(chipertext[i]) - 13) % 65 % 26 + 65))
                elif 97 <= ord(chipertext[i]) <= 122:
                    test.append(chr((ord(chipertext[i]) - 13) % 97 % 26 + 97))
                elif 48 <= ord(chipertext[i]) <= 57:
                    test.append(chr((ord(chipertext[i]) - 13) % 48 % 10 + 48))
                else:
                    test.append(chipertext[i])
        for i in range(len(key)):
            if i % 2 == 0:
                if 65 <= ord(key[i]) <= 90:
                    ky.append(chr((ord(key[i]) - 14) % 65 % 26 + 65))
                elif 97 <= ord(key[i]) <= 122:
                    ky.append(chr((ord(key[i]) - 14) % 97 % 26 + 97))
                elif 48 <= ord(key[i]) <= 57:
                    ky.append(chr((ord(key[i]) - 14) % 48 % 10 + 48))
                else:
                    ky.append(key[i])
                # ky.append(chr((ord(chipertext[i]) - 13) % 65 % 26 + 65))
            elif i % 5 == 0:
                if 65 <= ord(key[i]) <= 90:
                    ky.append(chr((ord(key[i]) - 17) % 65 % 26 + 65))
                elif 97 <= ord(key[i]) <= 122:
                    ky.append(chr((ord(key[i]) - 17) % 97 % 26 + 97))
                elif 48 <= ord(key[i]) <= 57:
                    ky.append(chr((ord(key[i]) - 17) % 48 % 10 + 48))
                else:
                    ky.append(key[i])
            elif i % 3 == 0:
                if 65 <= ord(key[i]) <= 90:
                    ky.append(chr((ord(key[i]) - 24) % 65 % 26 + 65))
                elif 97 <= ord(key[i]) <= 122:
                    ky.append(chr((ord(key[i]) - 24) % 97 % 26 + 97))
                elif 48 <= ord(key[i]) <= 57:
                        ky.append(chr((ord(key[i]) - 24) % 48 % 7 + 48))
                else:
                    ky.append(key[i])
            else:
                if 65 <= ord(key[i]) <= 90:
                    ky.append(chr((ord(key[i]) - 13) % 65 % 26 + 65))
                elif 97 <= ord(key[i]) <= 122:
                    ky.append(chr((ord(key[i]) - 13) % 97 % 26 + 97))
                elif 48 <= ord(key[i]) <= 57:
                    ky.append(chr((ord(key[i]) - 13) % 48 % 10 + 48))
                else:
                    ky.append(key[i])
        plain_mentah = ''.join(test)
        kunci1_mentah = ''.join(ky)
        kunci2_mentah = ky2
        hasil = DecCustomEnc(plain_mentah,kunci1_mentah,kunci2_mentah)
    return hasil

def DecCustomEnc(chipertext,key1,key2):
    alphabesar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphakecil = "abcdefghijklmnopqrstuvwxyz"
    angka = "1234567890"
    chipertext =[]
    kunci1 = []
    kunci2 = []
    for p in range(len(chipertext)):
        if 65 <= ord(chipertext[p]) <= 90:
            chipertext.append(alphabesar.find(chipertext[p]))
        elif 97 <= ord(chipertext[p]) <= 122:
            chipertext.append(alphakecil.find(chipertext[p]))
        elif 48 <= ord(chipertext[p]) <= 57:
            chipertext.append(angka.find(chipertext[p]))
        else:
            chipertext.append(chipertext[p])
    for k in range(len(chiper1)):
        if 65 <= ord(chiper1[k]) <= 90:
            kunci1.append(alphabesar.find(chiper1[k]))
        elif 97 <= ord(chiper1[k]) <= 122:
            kunci1.append(alphakecil.find(chiper1[k]))
        elif 48 <= ord(chiper1[k]) <= 57:
            kunci1.append(angka.find(chiper1[k]))
        else:
            kunci1.append(chiper1[k])
    # for k in range(len(chiper2)):
    #     if 65 <= ord(chiper2[k]) <= 90:
    #         kunci2.append(alphabesar.find(chiper2[k]))
    #     elif 97 <= ord(chiper2[k]) <= 122:
    #         kunci2.append(alphakecil.find(chiper2[k]))
    #     elif 48 <= ord(chiper2[k]) <= 57:
    #         kunci2.append(angka.find(chiper2[k]))
    #     else:
    #         kunci2.append(chiper[k])
    final = []
    if len(chipertext) == len(chiper1):
        for l in range(len(chipertext)):
            if 65 <= ord(chipertext[p]) <= 90:
                final.append(chr(ord(chipertext[i]) - chiper2 - (ord(chiper1[l])%65) % 26 + 65))

                # es = alphabesar.find(chipertext[i] +  ))
                # chipertext.append(alphabesar.find(chipertext[p]))
            elif 97 <= ord(chipertext[p]) <= 122:
                final.append(chr(ord(chipertext[i]) - chiper2 - (ord(chiper1[l])%97)  % 26 + 97))
                # chipertext.append(alphakecil.find(chipertext[p]))
            elif 48 <= ord(chipertext[p]) <= 57:
                final.append(chr(ord(chipertext[i]) - chiper2 - (ord(chiper1[l])%48)  % 10 + 48 ))
                # chipertext.append(angka.find(chipertext[p]))
            else:
                final.append(chr(chipertext[i] - chiper2 - (ord(chiper1[l]))))
                # chipertext.append(chipertext[p])
    else:
        for i n range(len(chipertext)):
            for j in range(len(chiper1)):
                if 65 <= ord(chipertext[i]) <= 90:
                    final.append(chr(ord(chipertext[i]) - chiper2 - (ord(chiper1[j])% 65) %26 + 65))
                elif 97 <= ord(chipertext[i]) <= 122:
                    final.append(chr(ord(chipertext[i]) - chiper2 - (ord(chiper1[j])% 97) %26 + 65))
                elif 48 <= ord(chipertext[i]) <= 57:
                    final.append(chr(ord(chipertext[i]) - chiper2 - (ord(chiper[j])% 48) %26 + 10))
                else:
                    final.append(chr(ord(chipertext[i]) - chiper2 ))

    return ''.join(final)




if __name__ == "__main__":
    app.run(host="0.0.0.0")
