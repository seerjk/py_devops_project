#!/bin/env python

name = "John"

# def sayHi(name, age=None, job):
    # SyntaxError: non-default argument follows default argument
def sayHi(name, job, age=None):
    "This program is developed by Jiangkun, it is mean to say hello."
    global address
    address = "Beijing"
    print address 

    print "Hello, my name is %s. I'm %s years old. What about you?" % (name, age)

    return "FunctionIsExcuted"


# print sayHi("Alex", 22, "IT")
# print address
# NameError: name 'address' is not defined
# sayHi("Jack", 33, "IT")
# sayHi("Rachel", "IT")

# if sayHi("Alex", 22, "IT") == "FunctionIsExcuted":
#     print "the program has been excuted successfully."


