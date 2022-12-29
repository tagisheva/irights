import requests
import constants
from re import search

_EXCLUDE_SYNC = "SYNC"
_EXCLUDE_REVERT = "Revert"

def __excludeIrrelevantTitles(idx_and_item):
    index, item = idx_and_item
    return not search(_EXCLUDE_SYNC, item["title"]) and not search(_EXCLUDE_REVERT, item["title"])

def getUserPRsListByDate(start_datetime, end_datetime):

    _start_filter = start_datetime.strftime("%Y-%m-%d")
    _end_filter = end_datetime.strftime("%Y-%m-%d") 

    _queryParams = "q=author:" + constants.USERNAME + "+type:pr+org:equinix-product+review:approved+state:closed+is:merged+merged:" + _start_filter + ".." + _end_filter

    _pull_requests_search = requests.get(constants.API_URL + "/search/issues", params=_queryParams, headers=constants.HEADERS)

    return filter(__excludeIrrelevantTitles, enumerate(_pull_requests_search.json()["items"]))

def getPRByUrl(url):
    return requests.get(url, headers=constants.HEADERS)
