import re

def find_match_in_file(search_term, file_location):

	try:
		
		with open(file_location) as line:
			for search in line:
				result = re.match(search_term, search)
				if result:
					return(result)
		return
	
	except Exception as err:
		print(err)