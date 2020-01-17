import json
import os

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
inflation_filename = os.path.join(SITE_ROOT, 'static/data', 'IPCA_BRL.json')


# Fazer casos de teste


def load_inflation_json():
    with open(inflation_filename) as test_file:
        return json.load(test_file)


def calc_money_value(money_value, year):
    money_value = float(money_value)
    inflation_dict = load_inflation_json()

    if int(year) < int(min(inflation_dict)):
        return "Year not in registered range"
    if money_value < 0:
        return "Money cannot be negative"

    for k_year in inflation_dict.keys():
        if int(year) <= int(k_year):
            money_value *= float(inflation_dict[k_year]) / 100 + 1
    return round(money_value, 2)


#print(calc_money_value(30, 1996))
