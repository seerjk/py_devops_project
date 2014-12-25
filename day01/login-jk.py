#!/usr/bin/env python

name = ''
password = ''
bl_name = ''
bl_num = 0
is_login = False

# read files:
# user.txt -- username password
# blacklist -- the user is locked
# f_user = file('user.txt')
# f_bl = file('blacklist', 'a+')


for i in range(3):
    # input user name
    name = raw_input('Please, input your user name: ').strip()

    # judge name is null
    if name == '':
        print 'user name is null!!!'
        continue

    # input password
    password = raw_input('Input your password: ')
    
    # judge the user name is in blacklist
    f_bl = file('blacklist.txt', 'r')

    for line in f_bl.readlines():
        line = line[0:-1]
        print 'locked name: %s, name is %s' % (len(line),len(name))
        print type(name), type(line)
        if name == line:
            print ''' Your user name is in blacklist.
                Please, contact with the administrator.
            '''
            break

        else:

            # judge username password is correct
            f_user = file('user.txt')
            f_bl = file('blacklist.txt', 'a+')

            for line in f_user.readlines():
                if name == line.split()[0]:
                    # name in user.txt
                    if password == line.split()[1]:
                        # password is correct
                        print '''
                            %s login.
                            Welcome.
                        ''' % (name)

                        is_login = True
                        break

                    else:
                        # password is incorrect
                        print 'Your password is incorrect!!'
                        if bl_num == 0:
                            bl_name = name
                            bl_num += 1
                        elif bl_name == name:
                            bl_num += 1
                        else:
                            bl_num = 0
    if is_login == True:
        break
else:
    if bl_num == 3:
        f_bl = file('blacklist.txt', 'a')
        f_bl.write(bl_name + "\n")
        print 'Your your user name %s is locked!!' % bl_name
        # judge bl_name was in the blacklist.txt


f_user.close()
f_bl.close()
