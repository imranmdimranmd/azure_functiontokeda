import csv
import os
from influxdb import InfluxDBClient

client = InfluxDBClient(host="localhost", port=8086)
client.switch_database("devsecops")

def load_fun(filename, measure, measure_name):
    file = open(filename) 
    reader = csv.DictReader(file)
    
    #Skip header
    next(reader)

    for row in reader:
        json_body=[{
        "measurement":measure_name,
        "tags":{"Severity":row[('Severity')]},
        "fields":{
        "Library":row[('PkgName')],
        "Vulnerability":row[('VulnerabilityID')],
        "Severity":row[('Severity')],
        "Installed Version":row[('InstalledVersion')],
       # "Fixed Version":row[4],          
        "Title":row[('Title')],
        "Description":row[('Description')],
        #"Passed":row[7]
        }
        }]
        client.write_points(json_body) 

load_fun("//opt/functiondemo/devsecops/leavedetails0.csv", "DATA: ", "trivy_leave")
load_fun("//opt/functiondemo/devsecops/leavedetails1.csv", "DATA: ", "trivy_leave")
load_fun("//opt/functiondemo/devsecops/leavedetails2.csv", "DATA: ", "trivy_leave")
load_fun("//opt/functiondemo/devsecops/leavedetails3.csv", "DATA: ", "trivy_leave")
load_fun("//opt/functiondemo/devsecops/leavedetails4.csv", "DATA: ", "trivy_leave")
load_fun("//opt/functiondemo/devsecops/leavedetails5.csv", "DATA: ", "trivy_leave")
load_fun("//opt/functiondemo/devsecops/leavedetails6.csv", "DATA: ", "trivy_leave")

print("done_cis")

