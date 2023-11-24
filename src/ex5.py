import csv
from pprint import pprint

def build_car_list():
    car_list = []
    id_model_mapping = dict()
    with open("files/car-ids.txt") as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            id_model_mapping.update({row[0]: row[1].strip()})

    with open("files/input.txt") as csv_file:
        rows = list(csv.reader(csv_file, delimiter=','))
        for row in rows[1:]:
            if float(row[1]) % 1.0 == 0.0:
                car_list.append({'id': int(row[0]), 'miles': int(row[1]), 'model': id_model_mapping.get(row[0])})

    return car_list

def ex5():
    car_list = build_car_list()
    pprint(car_list)