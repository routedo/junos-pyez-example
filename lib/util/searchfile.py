"""
Query file for search_term
"""

import re

def find_match_in_file(search_term, file_location):
    '''
    This function is used to query a file

    search_term = Term to find
    file_location = Location of file to query.
    '''

    try:

        with open(file_location) as line:
            for search in line:
                result = re.match(search_term, search)
                if result:
                    return result
        return

    except Exception as err:
        print(err)
