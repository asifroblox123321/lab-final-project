# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    #load a current view of the data
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()

    #check to see if year is in the query string portion of the URL
    requested_year = request.args.get('year')
    if requested_year == None:
        requested_year = "2020" #just in case

    #Filter and reformat data for ease of access in the template
    countries = list(data.keys())
    requested_data = {}
    for country in countries:
        requested_data[country] = data[country][requested_year]
    all_years = sorted(list(data[country].keys()))

    averageData = 0

    for country in countries:
        for key in data[country].keys():
            averageData += data[country][key]

    averageData = averageData/(len(all_years)*3)

    dottedPoints = [40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240]

    canadaPoints = ""
    mexicoPoints = ""
    usPoints = ""

    for key in data["Canada"].keys():
        canadaPoints = canadaPoints + str(40+((int(key)-1960)*3.5)) + "," + str(260-((int(data["Canada"][key]))*2)) + " "
        
    canadaPoints = canadaPoints[:-1]

    for key in data["Mexico"].keys():
        mexicoPoints = mexicoPoints + str(40+((int(key)-1960)*3.5)) + "," + str(260-((int(data["Mexico"][key]))*2)) + " "
        
    mexicoPoints = mexicoPoints[:-1]

    for key in data["United States"].keys():
        usPoints = usPoints + str(40+((int(key)-1960)*3.5)) + "," + str(260-((int(data["United States"][key]))*2)) + " "
        
    usPoints = usPoints[:-1]

    print(usPoints)

    return render_template('index.html', year=requested_year, all_years=all_years, data=requested_data, averageData = 260-(averageData*2), dottedPoints = dottedPoints, canadaPoints = canadaPoints, mexicoPoints = mexicoPoints, usPoints = usPoints)

@app.route('/year')
def year():
    #load a current view of the data
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()

    #check to see if year is in the query string portion of the URL
    requested_year = request.args.get('year')
    if requested_year == None:
        requested_year = "2020" #just in case

    #Filter and reformat data for ease of access in the template
    countries = list(data.keys())
    requested_data = {}
    for country in countries:
        requested_data[country] = data[country][requested_year]
    all_years = sorted(list(data[country].keys()))

    if 55 <= int(data["Canada"][requested_year]) < 57.5:
        canadaFill = "#ee0000"
    elif 57.5 <= int(data["Canada"][requested_year]) < 60:
        canadaFill = "#ee4600"
    elif 60 <= int(data["Canada"][requested_year]) < 62.5:
        canadaFill = "#ee8900"
    elif 62.5 <= int(data["Canada"][requested_year]) < 65:
        canadaFill = "#eebd00"
    elif 65 <= int(data["Canada"][requested_year]) < 67.5:
        canadaFill = "#eee300"
    elif 67.5 <= int(data["Canada"][requested_year]) < 70:
        canadaFill = "#d8ee00"
    elif 70 <= int(data["Canada"][requested_year]) < 72.5:
        canadaFill = "#b2ee00"
    elif 72.5 <= int(data["Canada"][requested_year]) < 75:
        canadaFill = "#a8ee00"
    elif 75 <= int(data["Canada"][requested_year]) < 77.5:
        canadaFill = "#6aee00"
    elif 77.5 <= int(data["Canada"][requested_year]) < 80:
        canadaFill = "#00c91b"
    elif 80 <= int(data["Canada"][requested_year]) < 82.5:
        canadaFill = "#007d11"


    if 55 <= int(data["Mexico"][requested_year]) < 57.5:
        mexicoFill = "#ee0000"
    elif 57.5 <= int(data["Mexico"][requested_year]) < 60:
        mexicoFill = "#ee4600"
    elif 60 <= int(data["Mexico"][requested_year]) < 62.5:
        mexicoFill = "#ee8900"
    elif 62.5 <= int(data["Mexico"][requested_year]) < 65:
        mexicoFill = "#eebd00"
    elif 65 <= int(data["Mexico"][requested_year]) < 67.5:
        mexicoFill = "#eee300"
    elif 67.5 <= int(data["Mexico"][requested_year]) < 70:
        mexicoFill = "#d8ee00"
    elif 70 <= int(data["Mexico"][requested_year]) < 72.5:
        mexicoFill = "#b2ee00"
    elif 72.5 <= int(data["Mexico"][requested_year]) < 75:
        mexicoFill = "#a8ee00"
    elif 75 <= int(data["Mexico"][requested_year]) < 77.5:
        mexicoFill = "#6aee00"
    elif 77.5 <= int(data["Mexico"][requested_year]) < 80:
        mexicoFill = "#00c91b"
    elif 80 <= int(data["Mexico"][requested_year]) < 82.5:
        mexicoFill = "#007d11"


    if 55 <= int(data["United States"][requested_year]) < 57.5:
        usFill = "#ee0000"
    elif 57.5 <= int(data["United States"][requested_year]) < 60:
        usFill = "#ee4600"
    elif 60 <= int(data["United States"][requested_year]) < 62.5:
        usFill = "#ee8900"
    elif 62.5 <= int(data["United States"][requested_year]) < 65:
        usFill = "#eebd00"
    elif 65 <= int(data["United States"][requested_year]) < 67.5:
        usFill = "#eee300"
    elif 67.5 <= int(data["United States"][requested_year]) < 70:
        usFill = "#d8ee00"
    elif 70 <= int(data["United States"][requested_year]) < 72.5:
        usFill = "#b2ee00"
    elif 72.5 <= int(data["United States"][requested_year]) < 75:
        usFill = "#a8ee00"
    elif 75 <= int(data["United States"][requested_year]) < 77.5:
        usFill = "#6aee00"
    elif 77.5 <= int(data["United States"][requested_year]) < 80:
        usFill = "#00c91b"
    elif 77.5 <= int(data["United States"][requested_year]) < 80:
        usFill = "#00c91b"
    elif 80 <= int(data["United States"][requested_year]) < 82.5:
        usFill = "#007d11"

    if int(data["United States"][requested_year]) >= int(data["Mexico"][requested_year]) >= int(data["Canada"][requested_year]):
        highest = "The United States"
        highestData = data["United States"][requested_year]
        medium = "Mexico"
        mediumData = data["Mexico"][requested_year]
        lowest = "Canada"
        lowestData = data["Canada"][requested_year]
    if int(data["United States"][requested_year]) >= int(data["Canada"][requested_year]) >= int(data["Mexico"][requested_year]):
        highest = "The United States"
        highestData = data["United States"][requested_year]
        medium = "Canada"
        mediumData = data["Canada"][requested_year]
        lowest = "Mexico"
        lowestData = data["Mexico"][requested_year]
    if int(data["Canada"][requested_year]) >= int(data["Mexico"][requested_year]) >= int(data["United States"][requested_year]):
        highest = "Canada"
        highestData = data["Canada"][requested_year]
        medium = "Mexico"
        mediumData = data["Mexico"][requested_year]
        lowest = "The United States"
        lowestData = data["United States"][requested_year]
    if int(data["Canada"][requested_year]) >= int(data["United States"][requested_year]) >= int(data["Mexico"][requested_year]):
        highest = "Canada"
        highestData = data["Canada"][requested_year]
        medium = "The United States"
        mediumData = data["United States"][requested_year]
        lowest = "Mexico"
        lowestData = data["Mexico"][requested_year]
    if int(data["Mexico"][requested_year]) >= int(data["United States"][requested_year]) >= int(data["Canada"][requested_year]):
        highest = "Mexico"
        highestData = data["Mexico"][requested_year]
        medium = "The United States"
        mediumData = data["United States"][requested_year]
        lowest = "Canada"
        lowestData = data["Canada"][requested_year]
    if int(data["Mexico"][requested_year]) >= int(data["Canada"][requested_year]) >= int(data["United States"][requested_year]):
        highest = "Mexico"
        highestData = data["Mexico"][requested_year]
        medium = "Canada"
        mediumData = data["Canada"][requested_year]
        lowest = "The United States"
        lowestData = data["United States"][requested_year]

    return render_template('year.html', year=requested_year, all_years=all_years, data=requested_data, canadaFill=canadaFill, mexicoFill=mexicoFill, usFill=usFill, highest=highest, highestData=highestData, medium=medium, mediumData=mediumData, lowest=lowest, lowestData=lowestData)

app.run(debug=True)