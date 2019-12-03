from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('school_scores.json') as sat_data:
        satData = json.load(sat_data)
    return render_template('home.html')
    
@app.route("/stateDemographics")
def render_state_dempgraphics():
    with open('school_scores.json') as sat_data:
        satData = json.load(sat_data)
    return render_template('stateDemographics.html')
    
@app.route("/income&gender")
def render_income_and_gender():
    with open('school_scores.json') as sat_data:
        satData = json.load(sat_data)
    return render_template('income&gender.html')
    
@app.route("/academics&GPA")
def render_academics_and_GPA():
    with open('school_scores.json') as sat_data:
        satData = json.load(sat_data)
        for states in satData:
            if states['Code'] = ['AL'] and state['Year'] = ['2015']:
                math = states['GPA']['Math']
                verabal = states['GPA']['Verbal']
    return render_template('academics&GPA.html')

if __name__=="__main__":
    app.run(debug=False)
