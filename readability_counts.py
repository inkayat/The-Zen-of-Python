"""
Giving meaningful names to variables, functions, modules, and classes; properly styling
blocks of code; using comments where necessary; keeping your code neat and elegant
– these all contribute to how readable and user-friendly your code is.
"""

#Bad
def f(i):
    l = i + (0.08 * i)
    return l

#Better
def calculate_gross_price(net_price):
    gross_price = net_price + (0.08 * net_price)
    return gross_price
