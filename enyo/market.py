import random as rand
import math
from datetime import datetime
from datetime import timedelta

def run_market_sim(inputs):
    output = []

    #inputs
    #Create an environment
    environment = Environment()
    #Generate the customers and add them to the environment
    for i in range(inputs["Customers"]["total"]):
        customer = Customer(i)
        customer.set_values(inputs["Customers"])
        environment.add_customer(customer)
    #Create the products
    for prod_info in inputs["Products"]:
        product = Product()
        product.set_values(prod_info)
        environment.add_product(product)
    #Create the organisations
    for org_info in inputs["Organisations"]:
        organisation = Organisation()
        organisation.set_values(org_info, environment.products)
        environment.add_org(organisation)

    for i in range(1000):
        rand_custs = rand.sample(environment.customers, len(environment.customers)/10)
        for customer in rand_custs:
            customer.decide_to_buy(environment.products.values())
            #print environment.products[1].n_sales
        if i % 100 == 0:
            n_multiprod_cust = 0
            for customer in environment.customers:
                if len(customer.prods_bought) > 0:
                    n_multiprod_cust += 1
            print 'multi cust', n_multiprod_cust
            for organisation in environment.organisations.values():
                scenarios = environment.check_scenario(organisation.org_id)
                scale_dp, scale_dq, scale_df = organisation.react_to_scenario(scenarios)
                for product in environment.products.values():
                    if not product.org_id == organisation.org_id:
                        continue
                    print scale_dp
                    product.change_attribs(scale_dp, scale_dq, scale_df)
        if i % 10 == 0:
            share = environment.calc_market_share(i)
        if i % 100 == 0:
            print share, environment.products[1].n_sales, environment.products[2].n_sales
        output.append(share)

    return output

class Customer(object):
    def __init__(self, cust_id):
        self.cust_id = cust_id
        self.p_util = 0
        self.q_util = 0
        self.f_util = 0
        self.buy_thresh = 0
        self.buy_thresh_var = 0
        self.prods_bought = []

    def set_values(self, cust_details):
        """
        Sets the intial customer details
        :param cust_details: (dict) Parameters set by the user to set the
        utility coefficients and the buying thresholds
        :return: void
        """
        r = rand.gauss(0, 1)
        if r < -2:
            buyer_type = "innovative"
        elif r < -1:
            buyer_type = "adopter"
        elif r < 0:
            buyer_type = "majority"
        elif r < 1:
            buyer_type = "conservative"
        else:
            buyer_type = "skeptic"
        assert buyer_type in cust_details.keys()
        self.p_util = cust_details[buyer_type]["p_util"]
        self.q_util = cust_details[buyer_type]["q_util"]
        self.f_util = cust_details[buyer_type]["f_util"]
        self.buy_thresh = cust_details["buy_thresh"]
        self.buy_thresh_var = cust_details["buy_thresh_var"]

    def decide_to_buy(self, products):
        """
        product.n_sales counter is incremented when the customer decides to buy
        the product and product.prod_id is appended to the customer.prods_bought
        list.
        :param products: (list) Products the customer has a choice of buying
        :return:void
        """
        max_pref = 0
        max_pref_prod = None
        for product in products:
            pref = math.sqrt(
                float(self.p_util * self.p_util) / (product.p * product.p) +
                self.q_util * self.q_util * product.q * product.q +
                self.f_util * self.f_util * product.f * product.f
            )
            #print product.prod_id, pref
            if pref > max_pref:
                max_pref = pref
                max_pref_prod = product
        if max_pref_prod == None:
            return
        if max_pref_prod.prod_id in self.prods_bought:
            return
        thresh = rand.gauss(self.buy_thresh, self.buy_thresh_var)
        if max_pref > thresh:
            self.prods_bought.append(max_pref_prod.prod_id)
            max_pref_prod.n_sales += 1
        #print max_pref_prod.n_sales
        #print temp


class Organisation(object):
    def __init__(self):
        self.org_id = 0
        self.prod_ids = []
        self.persona = "aggressive"

    def set_values(self, org_details, products):
        """
        Sets the intial customer details
        :param org_details: (dict) Parameters set by the user to set the
        personas of the organisation
        :param org_details: (list) All existing products. Used to check which
        organisation they belong to
        :return: void
        """
        self.org_id = org_details["org_id"]
        self.persona = org_details["persona"]
        for product in products.values():
            if self.org_id == product.org_id:
                self.prod_ids.append(product.prod_id)

    def add_product(self, prod_id):
        """
        If an organisation reacts by innovating a new product it will need to
        append the prod_id to its list of products
        :param prod_id:(int) product id
        :return:void
        """

    def react_to_scenario(self, scenarios):
        """
        This will set the scalings of the changes in the attributes
        :param scenarios:List of bools to say whether a scenario is true or
        false
        :return 3 floats scalings:
        """
        if self.persona == "competitive":
            if scenarios[0]:
                print self.org_id
                return 2., 1, 1,
        return 1., 1., 1.


class Product(object):
    def __init__(self):
        self.prod_id = 0
        self.org_id = 0
        self.p, self.q, self.f = 500, 500, 500
        self.p_limit, self.q_limit, self.f_limit = 400, 600, 600
        self.dp, self.dq, self.df = 10, 10, 10
        self.n_sales = 0

    def set_values(self, prod_details):
        """
        Sets the initial ids and attributes of the products
        :param prod_details: (dict) parameters set by the user to set the
        utility coefficients and the buying thresholds
        :return:void
        """
        self.p, self.q, self.f = prod_details["start_p"], prod_details["start_q"], prod_details["start_f"]
        self.p_limit, self.q_limit, self.f_limit = prod_details["limit_p"], prod_details["limit_q"], prod_details["limit_f"]
        self.dp, self.dq, self.df = prod_details["dp"], prod_details["dq"], prod_details["df"]
        self.prod_id = prod_details["prod_id"]
        self.org_id = prod_details["org_id"]

    def change_attribs(self, scale_dp, scale_dq, scale_df):
        """
        Change the attributes of the product if the organisation has to react to
        a scenario or just periodic changes. The attributes never go above or
        below their limits
        :param scale_dp: (float) scales the change in price
        :param scale_dq: (float) scales the change in quality
        :param scale_df: (float) scales the change in features
        :return:void
        """
        self.p = max(self.p_limit, self.p-self.dp*scale_dp, 0.01)
        self.f = min(self.f_limit, self.f+self.df*scale_df)
        self.q = min(self.q_limit, self.q+self.dq*scale_dq)


class Environment(object):
    def __init__(self):
        self.organisations = {}
        self.products = {}
        self.customers = []
        self.market_share = []

    def add_customer(self, customer):
        """
        Includes the customer to the environment.
        :param customer: (Customer object)
        :return:void
        """
        self.customers.append(customer)

    def add_product(self, product):
        """
        Includes the product to the environment. This maybe done in
        intialisation or during run-time of the simulation
        :param prod_id: (int) product id
        :param product: (Product object)
        :return:void
        """
        prod_id = product.prod_id
        self.products[prod_id] = product

    def add_org(self, org):
        """
        Includes the organisation to the environment. This maybe done in
        intialisation or during run-time of the simulation
        :param org_id: (int) organisation id
        :param org: (Oganisation object)
        :return:void
        """
        org_id = org.org_id
        self.organisations[org_id] = org

    def calc_market_share(self, i):
        """
        Calculates market share for all of the organisations in the
        environment.
        :param i: the iteration integer
        :return: dict of market share percentage for each organosation and the
        date
        """
        share = {
            "date": (datetime.today()+timedelta(days=i)).strftime("20%y-%m-%d")
        }
        hist_share = {"date": i}
        total_sales = 0
        for product in self.products.values():
            total_sales += product.n_sales
        for organisation in self.organisations.values():
            n_sales = 0
            for product in self.products.values():
                if product.prod_id in organisation.prod_ids:
                    n_sales += product.n_sales
            this_share = 0
            if total_sales > 0:
                this_share = float(n_sales)/total_sales*100
            share["Org%s" % str(organisation.org_id)] = str(this_share)
            hist_share[organisation.org_id] = this_share
        self.market_share.append(hist_share)
        return share

    def check_scenario(self, org_id):
        """
        Look at market history etc to see if there are any scenarios
        :return: list of bools
        """
        share_scenario = False
        latest_share = len(self.market_share) - 1
        earliest_share = max(len(self.market_share) - 100, 0)
        if len(self.market_share) > 100 and (self.market_share[earliest_share][org_id] - self.market_share[latest_share][org_id]) > 5:
            share_scenario = True
        return [share_scenario, False, False, False]
