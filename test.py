from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def root() : 
    return redirect(url_for('submit'))

@app.route('/submit/')
def submit() : 
    return render_template('form.html')
   
@app.route('/home', methods = ['POST'])
def home() : 
    mail = request.args.get('user-email')
    passw = request.args.get('user-password')
    return f'{mail} {passw}'