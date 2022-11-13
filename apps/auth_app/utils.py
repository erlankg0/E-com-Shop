import json


def get_province_by_country(name: str):
    provinces = open(f'json/province/{name}.json', 'r')
    data = json.load(provinces)[name]
    for item in range(len(data)):
        data[item] = tuple(data[item])
    return tuple(data)
