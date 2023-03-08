# Jira Request

export JIRA_TOKEN=123456789...
export JIRA_BASE_URL=https://jira.mms.org 

or 

JIRA_BASE_URL=https://jira.mms.org JIRA_TOKEN=mytoken python -m JiraRequest



```
 python JiraRequest.py -h
usage: JiraRequest.py [-h] [-u URL] [-t TOKEN] [-p PROJECT] [-i ISSUE]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Jira base URL (or environment variable JIRA_BASE_URL)
  -t TOKEN, --token TOKEN
                        Jira personal access token (or environment variable JIRA_TOKEN)
  -p PROJECT, --project PROJECT
                        Jira project key (e.g. QAUTO)
  -i ISSUE, --issue ISSUE
                        Jira issue key (e.g. QAUTO-1234)
```