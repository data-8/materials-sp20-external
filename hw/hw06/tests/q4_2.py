test = {   'name': 'q4_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> # The sample should be of size 200.;\n>>> representative_sample.num_rows == 200\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Your sample should have the same columns as the original table and all data in the sample should be present in the original table.;\n'
                                               ">>> all(np.in1d(representative_sample.column('mag'), earthquakes.column('mag')))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # The mean can't be bigger than the biggest magnitude, or smaller than the smallest!;\n"
                                               ">>> representative_mean < max(representative_sample.column('mag')) and representative_mean > min(representative_sample.column('mag'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
