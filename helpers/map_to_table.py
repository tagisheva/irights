from pickle import TRUE
import requests
import re
from re import search
from docxtpl import DocxTemplate, RichText

from helpers.constants import headers, JIRA, header_column_1, header_column_2, header_column_3, header_column_4

tpl=DocxTemplate("./files/template.docx")

def addTableHeader():
    return {"n": header_column_1, "cols": [RichText(header_column_2), RichText(header_column_3), RichText(header_column_4)]}

def getJiraTaskDataByBranchName(branch_name):
    hasStandartName = search("(-|\/)", branch_name)
    split_branch_name = re.split("(-|\/)", branch_name)

    return {
        "jira_project_key": split_branch_name[2] if hasStandartName else "",
        "jira_task_number": split_branch_name[4] if hasStandartName else ""
    }

def mapPullsIntoTableRows(idx_and_item):
    index, item = idx_and_item
    pull_url = item["pull_request"]["url"]
    pull_request = requests.get(pull_url, headers=headers)

    branch_name = pull_request.json()["head"]["ref"]
    jira_data = getJiraTaskDataByBranchName(branch_name)

    jira_project_key = jira_data["jira_project_key"]
    jira_task_number = jira_data["jira_task_number"]

    jira_task_url = ""
    if jira_task_number.isnumeric():
        jira_task_url = JIRA + jira_project_key + "-" + jira_task_number

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