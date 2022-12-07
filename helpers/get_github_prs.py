import requests
from re import search

from helpers.constants import GITHUB_USER, API_URL, headers, start_datetime, end_datetime

EXCLUDE_SYNC = "SYNC"
EXCLUDE_REVERT = "Revert"

def excludeIrrelevantTitles(idx_and_item):
    index, item = idx_and_item
    return not search(EXCLUDE_SYNC, item["title"]) and not search(EXCLUDE_REVERT, item["title"])

start_filter = start_datetime.strftime("%Y-%m-%d")
end_filter = end_datetime.strftime("%Y-%m-%d")

queryParams = "q=author:" + GITHUB_USER + "+type:pr+org:equinix-product+review:approved+state:closed+is:merged+merged:" + start_filter + ".." + end_filter

pull_requests_search = requests.get(API_URL + "/search/issues", params=queryParams, headers=headers)

pull_requests = filter(excludeIrrelevantTitles, enumerate(pull_requests_search.json()["items"]))