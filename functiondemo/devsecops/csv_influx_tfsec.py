import csv
import os
from influxdb import InfluxDBClient

client = InfluxDBClient(host="localhost", port=8086)
client.switch_database("devsecops")

def load_fun(filename, measure, measure_name):
    file = open(filename) 
    reader = csv.DictReader(file)

    #Skip header
    #next(reader)

    for row in reader:
        json_body=[{
        "measurement":measure_name,
        "tags":{
        "File":row[('file')],
        "Severity":row[('severity')],
        "RuleId":row[('rule_id')]
        },
        "fields":{
        "File":row[('file')],
        "StartLine":row[('start_line')],
        "EndLine":row[('end_line')],
        "RuleId":row[('rule_id')],
        "Severity":row[('severity')],          
        "Description":row[('description')],
        "Link":row[('link')],
        "Passed":row[('passed')]
        }
        }]
        client.write_points(json_body) 

#load_fun("/home/ec2-user/tfsec.csv", "DATA: ", "tfsec")
load_fun("/opt/functiondemo/devsecops/tfsec.csv", "DATA: ", "tfsec")
print("done_cis")


