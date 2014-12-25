#!/usr/bin/env python
# login version 2.0

import os
account_file = 'account.txt'
lock_file = 'lock.txt'

login_success = False

# put account in a list
f = file(account_file)
account_list = f.readlines()
f.close()

# put locked user into a lock list
# f = file(lock_file)
# lock_list = []
# for i in f.readlines():
#     lock_list.append(i.strip('\n'))
# 
# f.close()
# print lock_list

while True:
    username = raw_input('Username: ').strip()

    # put locked user into a lock list
    f = file(lock_file)
    lock_list = []
    for i in f.readlines():
        lock_list.append(i.strip('\n'))

    f.close()
    print lock_list

    if username in lock_list:
        print "Sorry, you are already in the block list, get the fucking out."
        break

    for line in account_list:
        line = line.split()

        if line[0] == username: # correct username
            for i in range(3):
                password = raw_input('Password: ').strip()
    
                if password == line[1]: # correct password
                    print "Welcome %s login my system!" % username
                    break
            
            else:
                print "Entered 3 times of wrong password, going to lock %s" % username
                f = file(lock_file, 'a')
                f.write('%s\n' % username)
                f.close()
            
            if login_success is True:
                # jump out of the top for loop
                break

    if login_success is True:
        # jump out of the while loop
        break
                
