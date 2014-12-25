#!/bin/env python

salary = 0

# goods list and price list
goods_list = ('ipad', 'macbook', 'iphone', 'vehicle', 'python cook book', 'cookie', 'pencil')
goods_price = (3500, 18000, 5300, 250000, 120, 5, 1)

shopping_list = []

# temp 
goods_id_to_buy = 0

# whether end shopping
end_shopping = False

# input your salary
salary = int(raw_input("Please, input your salary: ").strip())

while True:
    # print the goods list and price
    print "======================="
    print "The goods list:"
    for i in range(len(goods_price)):
        print "%s ---- %s" % (goods_list[i], goods_price[i])

    print "======================="

    # buy goods
    while True:
        try:
            goods_to_buy = raw_input("Input the goods that you want to buy: ")
            goods_id_to_buy = goods_list.index(goods_to_buy)

        except ValueError:
            print "The thing doesn't exist!!"

        else:
            break

    # The salary will be enough ?
    if salary >= goods_price[goods_id_to_buy]:
        # buy it, put the goods in shopping list
        salary -= goods_price[goods_id_to_buy]
        shopping_list.append(goods_list[goods_id_to_buy])
        print "You have bought the %s. You have $%s left." % (goods_list[goods_id_to_buy], str(salary))
    else:
        # salary is not enough
        print "You don't have enough money to buy %s. The price is $%s. But left of your salary is $%s. Word harder!!" % (goods_list[goods_id_to_buy], goods_price[goods_id_to_buy], salary)

    # whether continue shopping:
    while True:
        end = raw_input("Do you want to go home?(y/n)").strip()
        if end == 'y':
            end_shopping = True
            break
        elif end == 'n':
            break
        else:
            print "Input 'y' or 'n'."
    if end_shopping == True:
        # jump out of while loop
        break


# Output user's shopping list:
print "Your shopping list: "
# for i in range(len(shopping_list)):
#     print shopping_list[i]
shopping_list.sort()

print "======================"
for i in range(len(goods_list)):
    num = shopping_list.count(goods_list[i])
    print "%s --- %s" % (goods_list[i], str(num))

print "======================"

