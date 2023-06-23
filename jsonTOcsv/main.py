import json
import csv

inp_json_file = "jason.json"
out_csv_file = "outputcsv.csv"

json_data = None

with open(inp_json_file) as json_file:
    json_data = json.load(json_file)



