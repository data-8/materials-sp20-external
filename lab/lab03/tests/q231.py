test = {   'name': 'q231',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> # It looks like you're not making an array.  You shouldn't need to;\n"
                                               '>>> # use .item anywhere in your solution.;\n'
                                               '>>> type(population_magnitudes) == np.ndarray\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # You made an array, but it doesn't have the right numbers in it.;\n"
                                               '>>> sum(abs(population_magnitudes - np.log10(population_amounts))) < 1e-6\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
