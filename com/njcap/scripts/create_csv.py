import json
import csv
import numpy as np

equity_funds, debt_funds, other_funds = [],[],[]

with open("funds_stats/stats.json", "r") as f:
    stats_json = f.readline()
    stats_json = json.loads(stats_json)

for fund in stats_json:
    if fund["meta"]["scheme_category"].lower().split()[0] == 'equity':
        eq_obj = {}
        eq_obj.update(fund["meta"])
        eq_obj.update(fund["data"])
        equity_funds.append(eq_obj)
    elif fund["meta"]["scheme_category"].lower().split()[0] == 'debt':
        debt_obj = {}
        debt_obj.update(fund["meta"])
        debt_obj.update(fund["data"])
        debt_funds.append(debt_obj)
    else:
        other_obj = {}
        other_obj.update(fund["meta"])
        other_obj.update(fund["data"])
        other_funds.append(other_obj)

# Generate CSV

with open("csv/equity_funds.csv", "w") as equity_file:
    count = 0
    csv_writer = csv.writer(equity_file)
    for fund in equity_funds: 
        if count == 0: 

            # Writing headers of CSV file 
            header = fund.keys() 
            csv_writer.writerow(header) 
            count += 1

        # Writing data of CSV file 
        csv_writer.writerow(fund.values())

with open("csv/debt_funds.csv", "w") as debt_file:
    count = 0
    csv_writer = csv.writer(debt_file)
    for fund in debt_funds: 
        if count == 0: 

            # Writing headers of CSV file 
            header = fund.keys() 
            csv_writer.writerow(header) 
            count += 1

        # Writing data of CSV file 
        csv_writer.writerow(fund.values())

with open("csv/other_funds.csv", "w") as other_file:
    count = 0
    csv_writer = csv.writer(other_file)
    for fund in other_funds: 
        if count == 0: 

            # Writing headers of CSV file 
            header = fund.keys() 
            csv_writer.writerow(header) 
            count += 1

        # Writing data of CSV file 
        csv_writer.writerow(fund.values())
