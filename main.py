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
    else:
        element["quantity"] = int(element["quantity"])
    if element["revenue"] == "N/A":
        element["revenue"] = 0
    else:
        element["revenue"] = float(element["revenue"])

for region, tariff in dictionary.items():
    if tariff == "N/A":
        dictionary[region] = 0

for sales in list_of_dictionaries:
    for region, tariff in dictionary.items():
        if sales["region"] == region:
            sales["net_profit"] = sales["revenue"] - (sales["revenue"] * (tariff / 100))

fieldnames = list(list_of_dictionaries[0].keys())

with open("cleaned_sales_updated.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_of_dictionaries)

