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
        data = ''
        for states in satData:
            print('hi')
            if states['State']['Code'] == 'AL' and states['Year'] == 2015:
                for grade in states['GPA']:
                        data += '{ y: ' + str(states['GPA'][grade]['Math']) + ', label: ' + '"' + grade + "'" + ' },'
        print(data)
    return render_template('academics&GPA.html', mathScore = data)

if __name__=="__main__":
    app.run(debug=False)