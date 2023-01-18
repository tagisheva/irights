import constants_upd as constants
import helpers.map_to_table as helper
import api.get_github_prs as prs
import api.get_github_issues as issues

def createReport(today_datetime, start_datetime, end_datetime):
    table_data_pulls = map(helper.mapPullsIntoTableRows, prs.getUserPRsListByDate(start_datetime, end_datetime))

    table_data_issues = map(helper.mapIssuesIntoTableRows, issues.getIssuesByDate(start_datetime, end_datetime))

    tables_merged = list(table_data_pulls) + list(table_data_issues)

    table_data = map(helper.mapToTableData, list(enumerate(tables_merged)))

    tbl_contents = [helper.addTableHeader()] + list(table_data)

    start = start_datetime.strftime("%d %B %Y")
    end = end_datetime.strftime("%d %B %Y")
    today = today_datetime.strftime("%d %B %Y")

    context_dict = {
        "company": constants.COMPANY,
        "start_date": start,
        "end_date": end,
        "employee": constants.EMPLOYEE,
        "position": constants.POSITION,
        "manager": constants.MANAGER,
        "today": today,
        "tbl_contents": tbl_contents,
    }
    helper.tpl.render(context_dict)
    helper.tpl.save("files/" + today_datetime.strftime("%B") + ".docx")
