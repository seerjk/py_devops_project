#!/usr/bin/env python
import tab

n = 0
while n < 10:
# for i in range(3):
# while True:
# while False:
    n = n + 1
    print n
    name = raw_input('What is your name? ').strip()
    if len(name) == 0:
        continue
    break
    # print 'current loop:', i
else:
    print "Loop is done."

age = raw_input('What is your age? ')
sex = raw_input('What is your sex? ').strip()
# strip
job = raw_input('What is your job? ')
'''
print "Your name is %s, it's a good name." % name
print "Your name is %s, it's a good name." % "name"
print "Your name is %s, it's a good name." "name"
'''
print type(age)
age = int(age)

print """Personal Info:

    Name: %s
    Age : %d
    Sex : %s
    Job : %s
""" % (name, age, sex, job)

if age <= 28:
    print "You can have half day's public holiday!"
elif sex == 'F':
    print "Let me think about it ..."
else:
    print "You are too old to take this holiday!"
