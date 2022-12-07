import os
from load_env import load
import datetime

load

API_URL="https://api.github.com"
header_column_1="No."
header_column_2="Work description"
header_column_3="Co-author"
header_column_4="Work location"

ACCEPT=os.getenv('ACCEPT')
GITHUB_USER=os.getenv('GITHUB_USER')
TOKEN=os.getenv('TOKEN')
JIRA=os.getenv('JIRA')
MANAGER=os.getenv('MANAGER')
EMPLOYEE=os.getenv('EMPLOYEE')
POSITION=os.getenv('POSITION')
COMPANY=os.getenv('COMPANY')

print(GITHUB_USER)

headers = {
    "Authorization": "token " + TOKEN,
    "Accept": ACCEPT
}

start_day=1
today_day=29
end_day=29
month=12
year=2022

today_datetime = datetime.datetime(year, month, today_day)
start_datetime = datetime.datetime(year, month, start_day)
end_datetime = datetime.datetime(year, month, end_day)

#   "EIA_ORDERING_FLOW": {
#     "status": "enabled"
#   },
#   "EIA_FABRIC_ORDERING_FLOW": {
#     "status": "enabled"
#   },
#   "EIA_ROUTING_CONFIGURATION_V1": {
#     "status": "disabled"
#   },
#   "EIA_PRICES_SEARCH_V1": {
#     "status": "disabled"
#   },
#   "EIA_PORT_CONFIGURATION_V1": {
#     "status": "disabled"
#   },
#   "EIA_ADDITIONAL_IP_CONFIG_V1": {
#     "status": "disabled"
#   },
#   "EIA_BANDWIDTH_COMMIT_V1": {
#     "status": "disabled"
#   },
#   "EIA_PURCHASE_ORDER_V1": {
#     "status": "disabled"
#   },
#   "EIA_SERVICE_API": {
#     "status": "enabled"
#   },
#   "EIA_GITHUB_CONTENT": {
#     "status": "enabled"
#   },
#   "EIA_SIGNATURE_FLOW": {
#     "status": "disabled"
#   }
#   "EIA_ADD_PURCHASE_ORDER_V1": true
