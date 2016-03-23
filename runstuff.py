from enyo.environment import Company, Market

m = Market({"value": 50000000, "growth_rate": 0.1})

m.add_customers()
print len(m.customers)
m.grow()
print len(m.customers)