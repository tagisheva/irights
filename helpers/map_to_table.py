import re
from docxtpl import DocxTemplate, RichText

import constants_upd as constants
import api.get_github_prs as prs

tpl=DocxTemplate("./files/template.docx")

def __getJiraTaskDataByBranchName(branch_name):
    hasStandartName = re.search("(-|\/)", branch_name)
    split_branch_name = re.split("(-|\/)", branch_name)
    hasStandartLength = len(split_branch_name) > 4

    return {
        "jira_project_key": split_branch_name[2] if hasStandartName and hasStandartLength else "",
        "jira_task_number": split_branch_name[4] if hasStandartName and hasStandartLength else ""
    }

def addTableHeader():
    return {"n": constants.COL_TITLE_1, "cols": [RichText(constants.COL_TITLE_2), RichText(constants.COL_TITLE_3), RichText(constants.COL_TITLE_4)]}

def mapPullsIntoTableRows(idx_and_item):
    index, item = idx_and_item
    url = item["pull_request"]["url"]
    pull_request = prs.getPRByUrl(url)
    branch_name = pull_request.json()["head"]["ref"]
    jira_data = __getJiraTaskDataByBranchName(branch_name)

    jira_project_key = jira_data["jira_project_key"]
    jira_task_number = jira_data["jira_task_number"]

    jira_task_url = ""
    if jira_task_number.isnumeric():
        jira_task_url = constants.JIRA + jira_project_key + "-" + jira_task_number

    work_description_cell = RichText('')

    if jira_task_url!="":
        work_description_cell.add(jira_task_url,url_id=tpl.build_url_id(jira_task_url),color='#0000EE')
        work_description_cell.add("\a\n" + item["title"])
    else:
        work_description_cell.add(item["title"])

    co_author_cell = RichText('      ---')
    work_location_cell = RichText('')
    work_location_cell.add(item["html_url"],url_id=tpl.build_url_id(item["html_url"]),color='#0000EE')

    return { "n": str(index + 1) + ".", "cols": [work_description_cell, co_author_cell, work_location_cell]}


def mapIssuesIntoTableRows(idx_and_item):
    index, item = idx_and_item
    issue_url = item["html_url"]

    work_description_cell = RichText('')
    work_description_cell.add("\a\n" + item["title"])
    co_author_cell = RichText('      ---')
    work_location_cell = RichText('')
    work_location_cell.add(issue_url,url_id=tpl.build_url_id(issue_url),color='#0000EE')

    return { "n": str(index + 1) + ".", "cols": [work_description_cell, co_author_cell, work_location_cell]}

def mapToTableData(idx_and_item):
    index, item = idx_and_item

    return { "n": str(index + 1) + ".", "cols": item["cols"] }