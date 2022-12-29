import os
from load_env import load

load

API_URL="https://api.github.com"
WIKI_URL="https://equinixjira.atlassian.net"
JIRA="https://equinixjira.atlassian.net/browse/"
COL_TITLE_1="No."
COL_TITLE_2="Work description"
COL_TITLE_3="Co-author"
COL_TITLE_4="Work location"
ACCEPT="application/vnd.github+json"

USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')
TOKEN=os.getenv('TOKEN')
WIKI_TOKEN=os.getenv('WIKI_TOKEN')
WIKI_BASE_TOKEN=os.getenv('WIKI_BASE_TOKEN')
MANAGER=os.getenv('MANAGER')
EMPLOYEE=os.getenv('EMPLOYEE')
POSITION=os.getenv('POSITION')
COMPANY=os.getenv('COMPANY')

HEADERS = {
    "Authorization": "token " + TOKEN,
    "Accept": ACCEPT
}

WIKI_HEADERS = {
    "Authorization": "Basic " + WIKI_BASE_TOKEN,
    "Content-Type": "application/json"
}
