#!/usr/bin/env python
# by: JK
# version: 2.0

account_file = 'account.txt'
lock_file = 'lock.txt'
login_success = False

# put the username and password in account_list
f = file(account_file)
account_list = f.readlines()
f.close()

print account_list

login_success = False
username_locked = False

while True:
    username = raw_input("Input Username: ").strip()

    # judge username is in lock_file
    lock_list = []
    f = file(lock_file)
    
    for line in f.readlines():
        lock_list.append(line.strip('\n'))

    f.close()

    if username in lock_list:
        print "Your account '%s' was locked." % username
        break

    # 
    for line in account_list:
        line = line.strip('\n')
        # print line

        if username == line.split()[0]:
            # username is correct

            for i in range(3):
                # input password at most 3 times
                password = raw_input("Input your password: ").strip()

                if password == line.split()[1]:
                    # password is correct
                    print "Welcome %s login ERP system!" % username
                    login_success = True
                    break

                else:
                    print "Your password is wrong. Please input again."

            else:
                # input wrong password for 3 times. Lock the account.
                f = file(lock_file, 'a')
                f.write('%s\n' % username)
                f.close()
                print "3 times wrong!! Your account '%s' is locked." % username
                username_locked = True
                break

        if login_success == True or username_locked == True: break
        # jump out of the top for loop

    if login_success == True or username_locked == True: break
    # jump out of the while loop
                 