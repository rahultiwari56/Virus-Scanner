import os
import json
import requests
from flask import Flask, request, jsonify, render_template

from config import config
from src.send_email import Scan_Report

send_email = Scan_Report(config.email, config.e_pwd)

app = Flask(__name__)


#   Home-page
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/scan_file',methods=['POST'])
def scan_file():
    '''
        This function will send user input file to the api and fetch the generated report

        Input:
        - Accepts the input as email and text file
        
        Output:
            - It generates the scanned report
    '''
    if request.method == 'POST':

        file = request.files['file']
        #print(user_email)
        
        files = {'file': file}

        params = {'apikey': config.scan_api_key}

        response_scan = requests.post(config.scan_url, files=files, params=params)
        response_scan_json  = response_scan.json()

        parameters = {'apikey': config.scan_api_key, 
                        'resource': response_scan_json["resource"]}

        response_report = requests.get(config.scan_report_url, params=parameters)
        response_report_json = response_report.json()
        print(response_report_json)

        if ((response_report_json["scans"])["Fortinet"])["result"] is None:
            final = {
                "hash value" : response_report_json["md5"],
                "Fortinet Detection name": "Not Found",
                "Number of engines detected" : response_report_json["total"],
                "scan date": response_report_json["scan_date"]
            }
        else:
            final = {
                "hash value" : response_report_json["md5"],
                "Fortinet Detection name": ((response_report_json["scans"])["Fortinet"])["detected"],
                "Number of engines detected" : response_report_json["total"],
                "scan date": response_report_json["scan_date"]
            }


        # print(final)
        file_name = response_scan_json["resource"]
        with open(f'Scanned_Result/{file_name}.json', 'w') as openfile:
            json.dump(final, openfile)

        try:
            user_email = request.form['email']
            send_email.notify(file_name, user_email)
        except:
            pass

        return render_template('result.html', value1 = final)


    return 'Invalid'



@app.route('/status/<code>')
def status(code):

    try:
        # print(code)
        openfile = open(f'Scanned_Result/{code}.json', 'r')
        data = json.load(openfile) 

        return render_template('result.html', value1 = data)

    except:
        return 'Invalid'
   




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port = 8080)

    