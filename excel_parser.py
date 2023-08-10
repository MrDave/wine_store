import pandas
from pprint import pprint


wines = pandas.read_excel(
    "wine2.xlsx",
    keep_default_na=False,
).to_dict(orient="records")

categories = pandas.read_excel(
    "wine2.xlsx",
    keep_default_na=False,
    usecols="A",
).to_dict()["Категория"].values()


def sort_wines(wines, category):
    sorted_wines = []
    for wine in wines:
        if wine["Категория"] == category:
            sorted_wines.append(wine)
    return sorted_wines


inventory = {}

for category in categories:
    inventory[category] = sort_wines(wines, category)

pprint(inventory)
