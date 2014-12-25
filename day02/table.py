#/bin/env python

"""
two better ways to print a table
1. module: prettytable
    https://code.google.com/p/prettytable/wiki/Tutorial

2. pprint function

"""

from prettytable import PrettyTable

x = PrettyTable(["City name", "Area"])
x.align["city name"] = "l"
x.padding_width = 1
x.add_row(["Adelaide",1295])
x.add_row(["Adelaide",1295])
x.add_row(["Adelaide",1295])

print x

# --
x = PrettyTable()
x.add_column("City name", ["BJ", "XM", "HZ"])
x.add_column("Area", [1923, 1322, 1331])

print x
print "City name"
