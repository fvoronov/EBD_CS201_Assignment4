import csv
import json

with open("global_sales.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    list_of_dictionaries = list(reader)

with open("regional_tariffs.json", "r", encoding="utf-8") as f:
    dictionary = json.load(f)

for element in list_of_dictionaries:
    if element["quantity"] == "N/A":
        element["quantity"] = 0
    if element["revenue"] == "N/A":
        element["revenue"] = 0

for region, tariff in dictionary.items():
    if tariff == "N/A":
        dictionary[region] = 0

