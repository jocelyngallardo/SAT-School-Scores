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
    
def get_gender_scores():
    with open('school_scores.json') as sat_data:
        satData = json.load(sat_data)
        male = ''
        female = ''
        listOfStates = []
        for states in satData:
            if states['State']['Name'] == whichState and states['Year'] == 2015:
                for gender in states['Gender']:
                        female += Markup('{ y: ' + str(states['GPA']['Female']) + ', label: ' + '"' + grade + '"' + ' }' + ', ')
                        male += Markup('{ y: ' + str(states['GPA']['male']) + ', label: ' + '"' + grade + '"' + ' }' + ', ')
    return[dataMath.rstrip(', '), dataVerbal.rstrip(', ')]
#start of code for academics&GPA  
@app.route("/academics&GPA")
def render_academics_and_GPA():
    scores = get_scores('Alabama')
    return render_template('academics&GPA.html', mathScore = scores[0], verbalScore = scores[1], state = get_states(), stateName = 'Alabama')
 
@app.route("/academics&GPAreply")
def render_reply():
    scores = get_scores(request.args['states'])
    return render_template('academics&GPA.html', mathScore = scores[0], verbalScore = scores[1], state = get_states_reply(request.args['states']), stateName = request.args['states'])
    
def get_states():
    with open('school_scores.json') as sat_data:
        satData = json.load(sat_data)
        listOfStates = []
        option = ''
        for states in satData:
            if states['State']['Name'] not in listOfStates and states['Year'] == 2015:
                listOfStates.append(states['State']['Name'])
        for data in listOfStates:
            option = option + Markup("<option value=\"" + data + "\">" + data + "</option>")
    return option
      
def get_states_reply(state):
    with open('school_scores.json') as sat_data:
        satData = json.load(sat_data)
        listOfStates = []
        option = ''
        for states in satData:
            if states['State']['Name'] not in listOfStates and states['Year'] == 2015:
                listOfStates.append(states['State']['Name'])
        for data in listOfStates:
            option = option + Markup("<option value=\"" + data + "\">" + data + "</option>")
    return option     
 
def get_scores(whichState):
    with open('school_scores.json') as sat_data:
        satData = json.load(sat_data)
        dataMath = ''
        dataVerbal = ''
        listOfStates = []
        for states in satData:
            if states['State']['Name'] == whichState and states['Year'] == 2015:
                for grade in states['GPA']:
                        dataMath += Markup('{ y: ' + str(states['GPA'][grade]['Math']) + ', label: ' + '"' + grade + '"' + ' }' + ', ')
                        dataVerbal += Markup('{ y: ' + str(states['GPA'][grade]['Verbal']) + ', label: ' + '"' + grade + '"' + ' }' + ', ')
    return[dataMath.rstrip(', '), dataVerbal.rstrip(', ')]
#end of code for academics&GPA        

if __name__=="__main__":
    app.run(debug=False)
