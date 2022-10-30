import requests
import re
from docxtpl import DocxTemplate, RichText

from helpers.constants import headers, JIRA

tpl=DocxTemplate("./files/template.docx")

def mapPullsIntoTableRows(idx_and_item):
    index, item = idx_and_item
    pull_url = item["pull_request"]["url"]
    pull_request = requests.get(pull_url, headers=headers)
    split_branch_name = re.split("(-|\/)", pull_request.json()["head"]["ref"])
    project_key = split_branch_name[2]
    task_number = split_branch_name[4]
    task_url = ""
    if task_number.isnumeric():
        task_url = JIRA + project_key + "-" + task_number

    task_rt = RichText('')

    if task_url!="":
        task_rt.add(task_url,url_id=tpl.build_url_id(task_url),color='#0000EE')
        task_rt.add("\a\n" + item["title"])
    else:
        task_rt.add(item["title"])

    help_rt = RichText('      ---')
    github_rt = RichText('')
    github_rt.add(item["html_url"],url_id=tpl.build_url_id(item["html_url"]),color='#0000EE')

    return { "n": str(index + 1) + ".", "cols": [task_rt, help_rt, github_rt]}


def mapIssuesIntoTableRows(idx_and_item):
    index, item = idx_and_item
    issue_url = item["html_url"]

    task_rt = RichText('')
    task_rt.add("\a\n" + item["title"])
    help_rt = RichText('      ---')
    github_rt = RichText('')
    github_rt.add(issue_url,url_id=tpl.build_url_id(issue_url),color='#0000EE')

    return { "n": str(index + 1) + ".", "cols": [task_rt, help_rt, github_rt]}

def mapToTableData(idx_and_item):
    index, item = idx_and_item

    return { "n": str(index + 1) + ".", "cols": item["cols"] }