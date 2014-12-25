#/bin/env python

def square2(x):
    return x+x


a = [1,2,3,4,5]
b = [8,9]
c = [10,11,12]

print 'a:', a
print map(square2, a)
print map(square2, (a,b))
print map(None, a, b)
print map(None, a, b, c)
