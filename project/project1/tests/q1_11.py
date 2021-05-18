test = {   'name': 'q1_11',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Incorrect labels for columns;\n'
                                               '>>> t = stats_for_year(1990);\n'
                                               ">>> t.labels == ('geo', 'population_total','children_per_woman_total_fertility', 'child_mortality_under_5_per_1000_born')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> # Incorrect number of rows;\n>>> t = stats_for_year(1990);\n>>> t.num_rows == 50\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> print(stats_for_year(1960).sort('geo').take(np.arange(5, 50, 5)))\n"
                                               'geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born\n'
                                               'chn  | 644450173        | 3.99                               | 309\n'
                                               'egy  | 27072397         | 6.63                               | 312.8\n'
                                               'gha  | 6652285          | 6.75                               | 210.9\n'
                                               'ita  | 49714962         | 2.37                               | 52\n'
                                               'mex  | 38174114         | 6.78                               | 142.9\n'
                                               'npl  | 10056945         | 5.99                               | 327.1\n'
                                               'prk  | 11424179         | 4.58                               | 127.3\n'
                                               'tur  | 27553280         | 6.3                                | 249\n'
                                               'uzb  | 8789492          | 6.71                               | 175.7\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> print(stats_for_year(2010).sort('geo').take(np.arange(3, 50, 5)))\n"
                                               'geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born\n'
                                               'bra  | 198614208        | 1.84                               | 16.7\n'
                                               'deu  | 80435307         | 1.39                               | 4.2\n'
                                               'fra  | 62961136         | 1.98                               | 4.3\n'
                                               'irn  | 74253373         | 1.9                                | 19.2\n'
                                               'kor  | 49090041         | 1.27                               | 4.1\n'
                                               'mys  | 28119500         | 2                                  | 8.3\n'
                                               'phl  | 93038902         | 3.15                               | 31.9\n'
                                               'sdn  | 36114885         | 4.64                               | 80.2\n'
                                               'ukr  | 45647497         | 1.44                               | 11.8\n'
                                               'yem  | 23591972         | 4.5                                | 58.8\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
