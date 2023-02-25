'''
function_name.__name__.split('.')[-1].replace('get', 'df'): This code can be useful if you have a number of functions
that all retrieve data and you want to standardize the naming of the resulting dataframes. Here's an example:
'''


def get_sales_data():
    return [10, 20, 30]


def get_customer_data():
    return ['Alice', 'Bob', 'Charlie']


sales_df = get_sales_data()
customer_df = get_customer_data()

print(sales_df)
print(customer_df)

# Standardize the dataframe names
sales_df = get_sales_data.__name__.split('.')[-1].replace('get', 'df')
customer_df = get_customer_data.__name__.split('.')[-1].replace('get', 'df')

print(sales_df)
print(customer_df)
