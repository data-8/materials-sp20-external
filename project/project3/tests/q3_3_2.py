test = {   'name': 'q3_3_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> test_movie_correctness.labels == ('Title', 'Genre', 'Was correct')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> test_movie_correctness.num_rows == test_movies.num_rows\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure that test_movie_correctness does not modify the original test_movies table;\n'
                                               ">>> test_movie_correctness.group('Genre').column(1).item(0) == 20\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
