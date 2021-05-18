test = {   'name': 'q2_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> # It looks like you forgot to have your function return something.;\n>>> simulate_key_strike() is not None\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import string;\n'
                                               '>>> all([simulate_key_strike() in list(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(100)])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # It looks like you didn't use all the letters or numbers of the alphabet, or you used too many;\n"
                                               '>>> import numpy as np;\n'
                                               '>>> np.random.seed(22);\n'
                                               '>>> 62 >= len(np.unique([simulate_key_strike() for i in range(500)])) >= 45\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
