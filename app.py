from flask import Flask
from flask import request
import operations

ipca_app = Flask('ipca_app')


@ipca_app.route('/', methods=['GET'])
def calc_money_value_today_given_year():
    # How much var money in a given year is worth today
    if 'money_value' not in request.args or 'year' not in request.args:
        return 'Empty fields <br> Use example: /?money_value=20&year=1997'
    money_value = float(request.args.get('money_value', None))
    given_year = int(request.args.get('year', None))
    #currency = request.args.get('currency', default="BRL")
    #if currency != "BRL":
    #    return "Currency not registered"
    return str(operations.calc_money_value(money_value, given_year))


if __name__ == '__main__':
    ipca_app.run()
