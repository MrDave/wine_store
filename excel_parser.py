import pandas

from collections import defaultdict


def get_inventory(excel_file_path):
    wines = pandas.read_excel(
        excel_file_path,
        keep_default_na=False,
    ).to_dict(orient="records")

    inventory = defaultdict(list)

    for wine in wines:
        inventory[wine["Категория"]].append(wine)

    return inventory
