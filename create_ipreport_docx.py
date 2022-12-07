from datetime import datetime

from helpers.constants import COMPANY, MANAGER, EMPLOYEE, POSITION, today_datetime, start_datetime, end_datetime
from helpers.map_to_table import mapPullsIntoTableRows, mapIssuesIntoTableRows, mapToTableData, tpl, addTableHeader
from helpers.get_github_prs import pull_requests
from helpers.get_github_issues import issues

table_data_pulls = map(mapPullsIntoTableRows, pull_requests)

table_data_issues = map(mapIssuesIntoTableRows, issues)

tables_merged = list(table_data_pulls) + list(table_data_issues)

table_data = map(mapToTableData, list(enumerate(tables_merged)))

start = start_datetime.strftime("%d %B %Y")
end = end_datetime.strftime("%d %B %Y")
today = today_datetime.strftime("%d %B %Y")

print("start: " + start)
print("end: " + end)
print("today: " + today)

tbl_contents = [addTableHeader()] + list(table_data)

context_dict = {
    "company": COMPANY,
    "start_date": start,
    "end_date": end,
    "employee": EMPLOYEE,
    "position": POSITION,
    "manager": MANAGER,
    "today": today,
    "tbl_contents": tbl_contents,
}
tpl.render(context_dict)
tpl.save("files/" + today_datetime.strftime("%B") + ".docx")