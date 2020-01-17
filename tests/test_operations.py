from unittest import TestCase

import operations

# iPCA multiplication 5,233495576


class Test(TestCase):
    #def test_load_inflation_json(self):
    #    self.fail()

    def test_calc_money_value(self):
        self.assertEqual(operations.calc_money_value(47, 1995), 245.97)
        self.assertEqual(operations.calc_money_value(47, 1991), "Year not in registered range")
        self.assertEqual(operations.calc_money_value(587, 1994), "Year not in registered range")
        self.assertEqual(operations.calc_money_value(17, 2020), 17)
        self.assertEqual(operations.calc_money_value(17, 2019), 17.73)
        self.assertEqual(operations.calc_money_value(-17, 2020), "Money cannot be negative")
