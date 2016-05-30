import numpy as np
from enum import Enum
import heapq

class CustomerTypes(Enum):
    Innovator = 99
    Early_Adopter = 96.5
    Early_Majority = 83
    Late_Majority = 49
    Laggard = 15


class Product(object):

    def __init__(self):
        self.version = 0
        self.price = np.infinite
        self.innovation_points = 0.
        self.quality = 0.

    def change_params(self, params, bump_version=True):
        if bump_version:
            self.version += 1
        self.price = params.get('price', np.infinite)
        self.innovation_points = params.get('innovation', 0.)
        self.quality = params.get('quality', 0.)


class Company(object):
    def __init__(self, name, market__share):
        self.name = name
        self.market_share = market__share
        self.product = None
        self.type = None
        self.competitive_advantage = 0.
        self.industry_attractiveness = 0.
        self.environmental_stability = 0.
        self.financial_strength = 0.

        self.history = []

        self.customer_loyalty = 3
        self.space_params = {
            'competitive_advantage': {
                'market_share': 3,
                'product_quality': 3,
                'product_life_cycle': 3,  # late to early
                'product_replacement_cycle': 3, # variable to fixed
                'customer_loyalty': self.customer_loyalty,
                'know_how': 3,
                'vertical_integration': 3,
            },
            'industry_attractiveness': {
                'growth_potential': 3,
                'profit_potential': 3,
                'financial_stability': 3,
                'know_how': 3,
                'resource_utilization': 3,
                'capital_intensity': 3,
                'ease_of_entry': 3,
                'capacity_utilization': 3,
            },
            'environmental_stability': {
                'technological_changes': 3,
                'rate_of_inflation': 3,
                'demand_variability': 3,
                'barriers_to_entry': 3,
                'competitive_pressure': 3,
                'price_elasticity_of_demand': 3,
                'pressure_from_substitutes': 3
            },
            'financial_strength': {
                'ROI': 3,
                'leverage': 3,
                'liquidity': 3,
                'required_to_available_capital': 3,
                'cash_flow': 3,
                'ease_of_exit': 3,
                'risk_doing_business': 3, # much to little
                'inventory_turnover': 3,
            }
        }

    def set_space_params(self, args=None):
        # if args exist then add copy them to space params
        if args:
            for k in args:
                if self.space_params.get(k, None):
                    for k2 in args[k]:
                        if self.space_params[k].get(k2, None):
                            self.space_params[k][k2] = args[k][k2]
        # calculate the SPACE parameters
        for key in self.space_params:
            category_sum = 0
            for i, category in enumerate(self.space_params[key]):
                category_sum += self.space_params[key][category]
            setattr(self, key,  float(category_sum) / float(i + 1))

    def set_space_values(self, ca, ia, es, fs):
        self.competitive_advantage = ca
        self.industry_attractiveness = ia
        self.environmental_stability = es
        self.financial_strength = fs
        self._define_quadrant()

    def _define_quadrant(self):
        # TODO do this
        attrs = [self.competitive_advantage,
                 self.industry_attractiveness,
                 self.environmental_stability,
                 self.financial_strength]
        maxes = heapq.nlargest(2, attrs)
        ind1 = attrs.index(maxes[0])
        ind2 = attrs.index(maxes[2])

    def make_product(self, params):
        self.product = Product()
        self.product.change_params(params)

    def make_move(self):
        pass


class Customer(object):

    def __init__(self):
        self.type = None
        self.sensitivity = {
            'price': None,
            'quality': None,
            'features': None
        }
        self.product = None

        self._define_type()

    def decide_to_buy(self, companies):
        # TODO make parameters to buy
        scores = []
        for company in companies:
            temp_product = company.product
            score = 0.  # decided by loyalty, price , quality etc
            scores.append(score)
        product = companies[scores.index(max(scores))].product

    def _define_type(self):
        """
        Use diffusion of innovations model to decide the customer type
        """
        sigma = 1
        mean = 0
        r = np.random.normal(mean, sigma)
        if mean <= r < sigma:
            self.type = CustomerTypes.Late_Majority
        if r >= sigma:
            self.type = CustomerTypes.Laggard
        if -sigma <= r < mean:
            self.type = CustomerTypes.Early_Majority
        if -2 * sigma <= r < -sigma:
            self.type = CustomerTypes.Early_Adopter
        if r <= - 2 * sigma:
            self.type = CustomerTypes.Innovator


class Market(object):
    def __init__(self, args):
        self.growth_rate = args.get('growth_rate', 0.)
        self.value = args.get('market_value', 0.)
        self.customers = []

    def add_customers(self, n_customers=100000):
        """
        Adds customers to the market
        :param n_customers: How many to add to the market
        """
        for i in xrange(n_customers):
            cust = Customer()
            self.customers.append(cust)

    def grow(self):
        """
        Grows the market by adding more customers.
        """
        self.add_customers(int(len(self.customers) * self.growth_rate))


# class Strategy(object):
#
#     def __init__(self, product, params):
#         pass


class TheGame(object):

    def __init__(self, market, companies):
        self.market = market
        self.companies = companies[1:]
        self.ours = companies[0]

    def play(self):
        pass
