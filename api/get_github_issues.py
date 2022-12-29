import requests
import constants

def getIssuesByDate(start_datetime, end_datetime):
    _start_filter = start_datetime.strftime("%Y-%m-%d")
    _end_filter = end_datetime.strftime("%Y-%m-%d")

    _queryParams = "q=author:" + constants.USERNAME + "+type:issue+org:equinix-product+created:" + _start_filter + ".." + _end_filter

    _issues_search = requests.get(constants.API_URL + "/search/issues", params=_queryParams, headers=constants.HEADERS)

    return enumerate(_issues_search.json()["items"])