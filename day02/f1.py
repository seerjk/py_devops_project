#!/bin/env python
import time
import fileinput

f = open("f_test.txt")

"""
for line in fileinput.input('f_test.txt', inplace=1, backup='.bak'):
    line = line.replace("haha 34", "++++++++++")
    print line,
"""

"""
# for line in fileinput.input('f_test.txt', inplace=0):
for line in fileinput.input('f_test.txt'):
    line = line.replace("haha 34", "+++++++")
    print line,
"""

"""
for line in fileinput.input('f_test.txt', inplace=1):
    line = line.replace("the 4 loops", "chage me 4 loops")
    print line,
"""

"""
f = file("f_test.txt", 'r')
file_content = f.readlines()

print file_content
"""

"""
for i in range(0, 31):
    time.sleep(1)
    f.write('the %s loops\n' % i)
    f.flush()

time.sleep(10)
f.close()
"""
