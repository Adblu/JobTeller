from src import config as cfg
import csv

def clearCsv():
    f = open(cfg.csvResultsPath, "w+")
    f.close()

def dict2csv(data):
    with open(cfg.csvResultsPath, "a", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for item in data:
            writer.writerow([item["title"],
                             item["hiringOrganization"]["name"],
                             item["datePosted"],
                             item["validThrough"],
                             item["description"]
                             ])
