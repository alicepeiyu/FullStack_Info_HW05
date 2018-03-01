# Importing flask library
from app import app
from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
import os
app.secret_key = os.environ.get('SECRET_KEY') or 'hard to guess string'

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:        
        return render_template('survey.html', username=session['username'])
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST']) # You need to specify something here for the function to get requests
def login():
    # Here, you need to have logic like if there's a post request method, store the username and email from the form into
    # session dictionary
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['email'] = request.form['email']
    return redirect(url_for('index'))
    

    # if():
    #     pass
    # return None

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))

@app.route('/submit-survey', methods=['GET', 'POST'])
def submitSurvey():
    # print(123)
    # username = ''
    # email = ''
    # if(): #check if user in session
    if 'username' in session:
        # username = session.get('username')
        # print(123)
        # username = session['username']
        surveyResponse = {}
        #get the rest o responses from users using request library Hint: ~3 lines of code
        surveyResponse['color'] = request.form.get('color')
        surveyResponse['food'] = request.form.get('food')
        surveyResponse['vacation'] = request.form.get('vacation')
        surveyResponse['feBefore'] = request.form.get('feBefore')
        surveyResponse['feAfter'] = request.form.get('feAfter')
        return render_template('results.html', username=session['username'], surveyResponse=surveyResponse) # pass in variables to the template
    else:
        # print(123)
        return render_template('login.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
