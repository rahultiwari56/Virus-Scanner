
'''
    This is just a testing file
    But this file is not used in the project directly.
'''


import requests
from flask import jsonify 
import json

resp = '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b'


def scan():
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    params = {'apikey': ''}

    # files = {'file': ('a.txt', open('./uploaded/a.txt', 'rb'))}
    files = open('imp.txt', 'rb').read()
    # files = {'file': file}

    response_scan = requests.post(url, files=files, params=params)
    response_scan_json  = response_scan.json()
    
    return response_scan_json


def report():
    # resp_data = scan()
    # response_scan_json = resp_data["resource"]
    # response_scan_json = 'ed591b6b1eaca4ba4ed729b41fcd296c45b79151af4941aa32a4e5d78131aaf1'
    response_scan_json = "0496f4962d3dce3caa849f605749f7f2,82a02a0864447d51bb8c18ab4554a77e,e85463d19104cacd79a25cacb0b57c1d,ad04e313410dd865916b720e03e6b77e,4ad4f9b1e1e3e1f36b842645d1be716e,73d45bfefdef3a8b379887cf582a6105,2090a5cf258c81d08c284f4ca0e367a7,f0810b0186d0bfa77b42f8e30e9a966a"


    url = 'https://www.virustotal.com/vtapi/v2/file/report'

    parameters = {'apikey': '', 
                    'resource': response_scan_json}

    response_report = requests.get(url, params=parameters)
    response_report_json = response_report.json()

    with open(f'test.json', 'w') as openfile:
        json.dump(response_report_json, openfile)


    final = {
        "hash value" : response_report_json["md5"],
        "Fortinet Detection name": ((response_report_json["scans"])["Fortinet"])["detected"],
        "Number of engines detected" : response_report_json["total"],
        "scan date": response_report_json["scan_date"]
    }

    # print(final)
    return final

print(report())



