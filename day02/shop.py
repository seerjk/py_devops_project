#!/bin/env python

products = ['Car', 'iPhone', 'Bike', 'Coffee', 'PythonCourse']
prices = [500000, 4800, 800, 33, 5800]

salary = int(raw_input("Your current salary: "))

shopping_list = []

while True:
    print "On sale products: "
    for p in products:
        print p, prices[products.index(p)]

    option = raw_input("What do you want to buy?: ").strip()

    if len(option) == 0: continue

    if option in products:
        p_price = prices[products.index(option)]
        if salary >= p_price:
            print 'Adding \033[32;1m%s\033[0m into shopping list.' % option
            shopping_list.append(option)
            # salary = salary - p_price
            salary -= p_price
            print "Your current balance: \033[31;1m%s\033[0m " % salary
            continue

        else:
            print "\033[33;1mSorry, you cannot afford to buy %s\033[33;0m" % option

            if salary < min(prices):
                print "Too poor to buy anything from us, fuck off!"

                break

    
