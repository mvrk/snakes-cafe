print(
    """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************s
"""
)

# initialize empty meal dictionary

# start loop here until user enters quit

# create a variable to store the user's order
num_items = 0
order = ""
# order = input("> ")
orderList = []

while order != "quit":
    order = input("> ")
    orderList.append(order)
    num_items = orderList.count(order)
    report1 = f"** {num_items} order of {order} have been added to your meal **"
    report2 = f"** {num_items} orders of {order} have been added to your meal **"

    if num_items == 1:
        print(report1)
    else:
        print(report2)