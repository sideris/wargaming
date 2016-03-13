import numpy as np


class Company(object):
    def __init__(self, args):
        self.name = args.get('name', 'Unknown')


class Customers(object):

    def __init__(self):
        self.inclivity = np.random.normal()
        self.sensitivity = {
            'price': None,
            'quality': None,
            'features': None
        }


class Market(object):
    def __init__(self, args):
        self.growth_rate = args.get('growth_rate', 0.)
        self.value = args.get('market_value', 0.)
        self.customers = []

    def add_customers(self, customers=[]):
        """

        :param customers:
        """
        self.customers.extend(customers)
