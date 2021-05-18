test = {   'name': 'q3_2_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> from collections import Counter;\n'
                                               ">>> g = train_movies.column('Genre');\n"
                                               ">>> r = np.where(test_movies['Title'] == 'tron')[0][0];\n"
                                               '>>> t = test_my_features.row(r);\n'
                                               '>>> tron_expected_genre = Counter(np.take(g, np.argsort(fast_distances(t, train_my_features))[:13])).most_common(1)[0][0];\n'
                                               '>>> tron_genre == tron_expected_genre\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
