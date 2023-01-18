import os
from load_env import load

load

API_URL="https://api.github.com"

COL_TITLE_1="No."
COL_TITLE_2="Work description"
COL_TITLE_3="Co-author"
COL_TITLE_4="Work location"
ACCEPT="application/vnd.github+json"

WIKI_URL=os.getenv('WIKI_URL')
JIRA=os.getenv('JIRA')

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
