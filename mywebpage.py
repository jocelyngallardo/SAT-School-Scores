from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('school_scores.json') as sat_data:
        satData = json.load(sat_data)
        print(get_states)
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
        dataMath = ''
        dataVerbal = ''
        listOfStates = []
        for states in satData:
            if states['State']['Code'] =='AL'and states['Year'] == 2015:
                for grade in states['GPA']:
                        dataMath += Markup('{ y: ' + str(states['GPA'][grade]['Math']) + ', label: ' + '"' + grade + '"' + ' }' + ',')
                        dataVerbal += Markup('{ y: ' + str(states['GPA'][grade]['Verbal']) + ', label: ' + '"' + grade + '"' + ' }' + ',')
        print(dataMath.rstrip(','))
        print(dataVerbal.rstrip(','))
    return render_template('academics&GPA.html', mathScore = dataMath, verbalScore = dataVerbal)
    
def get_states():
    with open('school_scores.json') as sat_data:
        satData = json.load(sat_data)
        listOfStates = []
        option = ''
        for states in satData:
            if states['State']['Name'] not in listOfStates and states['Year'] == 2015:
                listOfStates.append(states['State']['Name'])
        for data in listOfStates:
            option = option + Markup("<option value=\"" + states + "\">" + states + "</option>")
    return option
        
        
if __name__=="__main__":
    app.run(debug=False)