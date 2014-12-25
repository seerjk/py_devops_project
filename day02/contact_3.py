# !/bin/env python
"""
ver: 2.0
fix bug: dratio print two same record
add: print searching result in a table. S.ljust()

version: 3.0
add: print table line
"""

def high_light_sub(s, sub):
    s_index = s.find(sub)
    return s[:s_index] + "\033[32;1m%s\033[0m" %sub + s[s_index+len(sub):]

def max_str_len_in_list(l):
    """
    Return the max length of the strings in a list 'l'.

    input: l a list
    return: the max length of strings
    """
    n_l = []
    for i in range(len(l)):
        n_l.append(len(l[i]))
    return max(n_l)

def print_table(dic, key_word=None):
    """
    print the dictionary as a table and highlight the key word.

    input: the dic, and key word
    return: None
    """

    # judge the dic is empty
    if dic == {}:
        print "the dic is empty."
        return False

    # Calculate the size of each column in the tables
    # column sizes: name, phone, company, email
    c_size = []

    # 
    c_size.append(max_str_len_in_list(dic.keys()))

    # the column of values:
    c_values = len(dic.values()[0])

    for i in range(c_values):
        # get the whole column of the item i in dic.values as a list
        c_list = sum(dic.values(),[])[i::c_values]
        # the length of each items in the list
        len_list = []
        for j in range(len(c_list)):
            len_list.append(len(c_list[j]))

        c_size.append(max(len_list))
    
    # Print the table:
    space = 4
    print '+' + ''.ljust(c_size[0]+space, '-') + '+' + '-'.ljust(c_size[1]+space, '-') + '+' + '-'.ljust(c_size[2]+space, '-') + '+' + '-'.ljust(c_size[3]+space, '-') + '+'

    print '|' + 'Name'.ljust(c_size[0]+space) + '|' + 'Phone'.ljust(c_size[1]+space) + '|' + 'Company'.ljust(c_size[2]+space) + '|' + 'E-mail'.ljust(c_size[3]+space) + '|'

    print '+' + '-'.ljust(c_size[0]+space, '-') + '+' + '-'.ljust(c_size[1]+space, '-') + '+' + '-'.ljust(c_size[2]+space, '-') + '+' + '-'.ljust(c_size[3]+space, '-') + '+'

    row = len(dic.keys())
    for i in range(row):
        print '|' + dic.keys()[i].ljust(c_size[0]+space) + '|' + dic.values()[i][0].ljust(c_size[1]+space) + '|' + dic.values()[i][1].ljust(c_size[2]+space) + '|' + dic.values()[i][2].ljust(c_size[3]+space) + '|'

    print '+' + '-'.ljust(c_size[0]+space, '-') + '+' + '-'.ljust(c_size[1]+space, '-') + '+' + '-'.ljust(c_size[2]+space, '-') + '+' + '-'.ljust(c_size[3]+space, '-') + '+'

    
# --------------------------------

contact_dic = {}
with open('contacts_list2.txt') as f:
    for i in f.readlines():
        line = i.strip().split()
        # print line
        contact_dic[line[0]] = line[1:]

# print contact_dic.keys()
# print_table(contact_dic)

while True:
    search = raw_input("Search info: ").strip()
    if len(search) == 0: continue # not empty input
    if contact_dic.has_key(search):
        print search, contact_dic[search]
    else:
        # start to search the info in fuzzy matching mode
        # records counter:
        info_counter = 0        

        if len(search) < 3:
            print "No valid info..."
            continue

        # search result dic: r_dic
        r_dic = {}

        for name, value in contact_dic.items():
            if name.count(search) != 0:
                # key fuzzy matching. Agui exsits
                # print name, value
                # s_index = name.find(search)

                # print name[:s_index] + "\033[32;1m%s\033[0m" %search + name[s_index+len(search):], '\t'.join(value)
                
                # print high_light_sub(name, search), '\t'.join(value)
                r_dic[name] = value

                # print "len: ", len(high_light_sub(name, search))
                info_counter += 1
                # if the same string is both in name and email address, there is the same record.
                continue

            for i in value:
                # second layer loop
                if i.count(search) != 0:
                    # print name, value
                    # print name, '\t'.join(value)
                    r_dic[name] = value
                    info_counter += 1

                    break

        # print the result:
        print_table(r_dic)

        if info_counter == 0:
            print "No valid record...."
        else:
            print "Found %s records..." % info_counter


"""
if contact_dic.has_key('Alex'):
    print ".."
else:
    for name, value in contact_dic.items():
        if 'Alex' in value: print "got you"
        else: print "no valid record."
"""
