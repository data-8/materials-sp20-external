test = {   'name': 'q3_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> full_data.num_rows -- 562\n1124', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # Double check the way you're combining the two tables. Are you combining in the correct order (in terms of the arguments)?;\n"
                                               '>>> # The problem statement saying "except \'Name\' column" is a hint at the order in which you should combine the tables.;\n'
                                               ">>> list(full_data.labels)[0] == 'Player'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> full_data.select(sorted(full_data.labels)).sort(4).take(range(3)).column(0).item(0) == 0.6\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
