#/bin/env python

import pickle

name_list = {
    'alex': [29, 'IT'],
    'Rain': {
        'age': 24,
        'job': 'saleman'
    },
    'jack': 999
}

# f = file('name_list.pkl', 'wb')
# pickle.dump(name_list, f)
# f.close()

with file('name_list.pkl', 'wb') as f:
    pickle.dump(name_list, f)

