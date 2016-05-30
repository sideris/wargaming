from enyo.environment import Company, Market, TheGame

market = Market({'market_value': 1000000000000, 'growth_rate': 0.1})
market.add_customers()

our_company = Company('ours', .4)
our_company.set_space_params({
            'competitive_advantage': {
                'market_share': 5,
                'product_quality': 4,
                'product_life_cycle': 2,
                'product_replacement_cycle': 3,
                'customer_loyalty': 4,
                'know_how': 4,
                'vertical_integration': 3,
            },
            'industry_attractiveness': {
                'growth_potential': 4,
                'profit_potential': 4,
                'financial_stability': 4,
                'know_how': 4,
                'resource_utilization': 3, # inefficient to efficient
                'capital_intensity': 3,
                'ease_of_entry': 5, # easy to difficult
                'capacity_utilization': 4,
            },
            'environmental_stability': {
                'technological_changes': 2,
                'rate_of_inflation': 3,
                'demand_variability': 3,
                'barriers_to_entry': 4,
                'competitive_pressure': 2,
                'price_elasticity_of_demand': 1,
                'pressure_from_substitutes': 4
            },
            'financial_strength': {
                'ROI': 5,
                'leverage': 3,
                'liquidity': 2,
                'required_to_available_capital': 2,
                'cash_flow': 4,
                'ease_of_exit': 5,
                'risk_doing_business': 4,
                'inventory_turnover': 4,
            }
})

other_company = Company('other1', .4)
other_company.set_space_params({
            'competitive_advantage': {
                'market_share': 5,
                'product_replacement_cycle': 3,
                'product_quality': 4,
                'product_life_cycle': 2,
                'customer_loyalty': 4,
                'know_how': 4,
                'vertical_integration': 3,
            },
            'industry_attractiveness': {
                'growth_potential': 4,
                'profit_potential': 4,
                'financial_stability': 4,
                'know_how': 4,
                'resource_utilization': 3, # inefficient to efficient
                'capital_intensity': 3,
                'ease_of_entry': 5, # easy to difficult
                'capacity_utilization': 4,
            },
            'environmental_stability': {
                'technological_changes': 2,
                'rate_of_inflation': 3,
                'demand_variability': 3,
                'barriers_to_entry': 4,
                'competitive_pressure': 2,
                'price_elasticity_of_demand': 1,
                'pressure_from_substitutes': 4
            },
            'financial_strength': {
                'ROI': 5,
                'leverage': 3,
                'liquidity': 2,
                'required_to_available_capital': 2,
                'cash_flow': 4,
                'ease_of_exit': 5,
                'risk_doing_business': 4,
                'inventory_turnover': 4,
            }
})

other_company2 = Company('other2', .2)
other_company2.set_space_params({
            'competitive_advantage': {
                'market_share': 2,
                'product_replacement_cycle': 2,
                'product_quality': 2,
                'product_life_cycle': 3,
                'customer_loyalty': 4,
                'know_how': 4,
                'vertical_integration': 3,
            },
            'industry_attractiveness': {
                'growth_potential': 4,
                'profit_potential': 4,
                'financial_stability': 4,
                'know_how': 4,
                'resource_utilization': 3, # inefficient to efficient
                'capital_intensity': 3,
                'ease_of_entry': 5, # easy to difficult
                'capacity_utilization': 4,
            },
            'environmental_stability': {
                'technological_changes': 2,
                'rate_of_inflation': 3,
                'demand_variability': 3,
                'barriers_to_entry': 4,
                'competitive_pressure': 2,
                'price_elasticity_of_demand': 1,
                'pressure_from_substitutes': 4
            },
            'financial_strength': {
                'ROI': 5,
                'leverage': 3,
                'liquidity': 2,
                'required_to_available_capital': 2,
                'cash_flow': 4,
                'ease_of_exit': 5,
                'risk_doing_business': 4,
                'inventory_turnover': 4,
            }
})
# TODO add products
thegame = TheGame(market, [our_company, other_company, other_company2])