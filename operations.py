import json
import os

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
inflation_filename = os.path.join(SITE_ROOT, 'static/data', 'IPCA_BRL.json')

# Fazer casos de teste

def load_inflation_json():
    with open(inflation_filename) as test_file:
        return json.load(test_file)


def calc_money_value(money_value, year):
    inflation_dict = load_inflation_json()
    for k_year in inflation_dict.keys():
        if year < int(k_year):
            money_value *= (float(inflation_dict[k_year]) / 100 + 1)
    return money_value


print(calc_money_value(5, 2001))
