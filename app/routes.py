
from app import app 
from .services import getProduct


from flask import render_template

@app.route('/')
def homePage():
    print(getProduct())
    return render_template('index.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')