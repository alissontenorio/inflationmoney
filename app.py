from flask import Flask
from flask import request
import operations

app = Flask(__name__)


@app.route('/', methods=['GET'])
def calc_money_value_today_given_year():
    # How much var money in a given year is worth today
    money_value = float(request.args.get('money_value', None))
    given_year = int(request.args.get('year', None))
    currency = request.args.get('currency', default="BRL")

    #if currency != "BRL":
    #    return "Currency not registered"

    return str(operations.calc_money_value(money_value, given_year))


if __name__ == '__main__':
    app.run()
