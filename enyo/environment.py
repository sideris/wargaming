import numpy as np


class Company(object):
    def __init__(self, name):
        self.name = name
        self.competitive_advantage = 0.
        self.industry_attractiveness = 0.
        self.environmental_stability = 0.
        self.financial_strength = 0.

        self.customer_loyalty = 3
        self.space_params = {
            'competitive_advantage': {
                'market_share': 3,
                'product_quality': 3,
                'product_life_cycle': 3,
                'customer_loyalty': self.customer_loyalty,
                'know_how': 3,
                'vertical_integration': 3,
            },
            'industry_attractiveness': {
                'growth_potential': 3,
                'profit_potential': 3,
                'financial_stability': 3,
                'know_how': self.space_params['competitive_advantage']['know_how'],
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
                'risk_doing_business': 3,
                'inventory_turnover': 3,
            }
        }

    def set_space_params(self, args):
        pass

    def set_space_values(self, ca, ia, es, fs):
        self.competitive_advantage = ca
        self.industry_attractiveness = ia
        self.environmental_stability = es
        self.financial_strength = fs


class Customer(object):

    def __init__(self):
        self.inclination = np.random.normal()
        self.loyalty = 0.
        self.sensitivity = {
            'price': None,
            'quality': None,
            'features': None
        }

        self.product = None


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


