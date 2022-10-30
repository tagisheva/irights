import requests

from helpers.constants import GITHUB_USER, API_URL, headers, start_datetime, end_datetime

start_filter = start_datetime.strftime("%Y-%m-%d")
end_filter = end_datetime.strftime("%Y-%m-%d")

queryParams = "q=author:" + GITHUB_USER + "+type:issue+org:equinix-product+created:" + start_filter + ".." + end_filter

issues_search = requests.get(API_URL + "/search/issues", params=queryParams, headers=headers)

issues = enumerate(issues_search.json()["items"])