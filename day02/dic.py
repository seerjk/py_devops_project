#!/bin/env python

contact_dic = {}
with open('contacts_list2.txt') as f:
    for i in f.readlines():
        line = i.strip().split()
        # print line
        contact_dic[line[0]] = line[1:]

print contact_dic.keys()

if contact_dic.has_key('Alex'):
    print ".."
else:
    for name, value in contact_dic.items():
        if 'Alex' in value: print "got you"
        else: print "no valid record."
    

"""
contacts = {
    'Alex' : 13651054608,
    'Rachel' : [13813743131, 'student', 25],
    'Rain' : {'age':28},
}

if contacts.has_key('Rain'): print "has Rain"

# R* include in a string
for i in contacts:
    print i,i.count('R')

# change value
contacts['Alex'] = 13307887878
# Add new item
contacts['Alex Li'] = 133011118
# del item
del contacts['Alex']

contacts.keys()
contacts.values()

contacts.popitem()

for i in contacts:
    print i

for i in contacts.items():
    print i

for k,v in contacts.items():
    print k,v
"""
