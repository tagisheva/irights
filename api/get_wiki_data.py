import requests

import constants

# from common list api I cannot get any data valuable for template, 
# looks like the viki itself uses cgraphql requests, 
# so to reach it from the outside I need to figure out how to orgonize authentication properly 

get_wiki_data = requests.get(constants.WIKI_URL + "/wiki/rest/recentlyviewed/1.0/recent", headers=constants.WIKI_HEADERS)

print(get_wiki_data.json())
