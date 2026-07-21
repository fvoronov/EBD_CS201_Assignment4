import csv
import json

with open("global_sales.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    list_of_dictionaries = list(reader)

with open("regional_tariffs.json", "r", encoding="utf-8") as f:
    dictionary = json.load(f)

