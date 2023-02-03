import csv
import json
import os

ads_csv = os.path.join("datasets", "ads.csv")
ads_json = os.path.join("fixtures", "ads.json")
categories_csv = os.path.join("datasets", "categories.csv")
categories_json = os.path.join("fixtures", "categories.json")


def category_to_json(csv_file, json_file):
    data_list = []

    with open(csv_file, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for rows in csv_reader:
            data_dict = {"model": "ads.category", "pk": rows["id"], "fields": rows}
            data_list.append(data_dict)
    with open(json_file, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(data_list, indent=4, ensure_ascii=False))


def ads_to_json(csv_file, json_file):
    data_list = []

    with open(csv_file, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for rows in csv_reader:
            rows["is_published"] = rows["is_published"].capitalize()
            data_dict = {"model": "ads.advertisement", "pk": rows["id"], "fields": rows}
            data_list.append(data_dict)
    with open(json_file, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(data_list, indent=4, ensure_ascii=False))


ads_to_json(ads_csv, ads_json)
category_to_json(categories_csv, categories_json)
