#!/usr/bin/env python
# login version 1.0

account_file = 'account.txt'
lock_file = 'lock.txt'
username_in = False

for i in range(3):
    if username_in == False:
        username = raw_input("username:").strip()

    password = raw_input("password:").strip()

    if len(username) != 0 and len(password) != 0:
        f = file(account_file)
        login_success = False
        
        for line in f.readlines():
            line = line.split()
            # if username == line.split()[0] and password == line.split()[1]:
            if username == line[0] and password == line[1]:
                # user and password are correct
                print "Welcome %s login my system." % username

                login_success = True
                break

            elif username == line[0]:
                # username is in account.txt, but password is wrong.
                username_in = True
                print "Wrong password!"


        print login_success
        if login_success is True: # login successfully
            break

    else:
        continue
else:
    f = file(lock_file, 'a')
    f.write('%s\n' % username)
    f.close()

