import os
import sys
import argparse
import json
import requests

# configure arguments
args = sys.argv[1:]
print("args:", args)

# use argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--issue', required=True, help="Jira issue key; required (e.g. QAUTO-1234)")
parser.add_argument('-t', '--token', required=False, help="Jira personal access token; optional (or set environment variable JIRA_TOKEN)")
args = parser.parse_args()
print("args:", args)
print("issue:", args.issue)

# get parameters
JIRA_TOKEN = args.token or os.getenv("JIRA_TOKEN")
print("JIRA_TOKEN:", JIRA_TOKEN)
if not JIRA_TOKEN:
    print("JIRA_TOKEN must be set")
    exit()

TEST_KEY = args.issue
if not TEST_KEY:
    print("TEST_KEY must be set")
    exit()


# URL info
JIRA_BASE_URL = "https://jira.mms.org"
JIRA_API_PATH = "rest/api/latest"
# ZEPHYR_API_PATH = "rest/zapi/latest"

REPORT_ENDPOINT = "report"
ISSUE_ENDPOINT = "issue"

# build url
url = f"{JIRA_BASE_URL}/{JIRA_API_PATH}/{ISSUE_ENDPOINT}/{TEST_KEY}"
print("url:", url)

# add authorization header
headers = {}
headers["Authorization"] =  f"Bearer {JIRA_TOKEN}"
print("headers:", headers)

# get request
response = requests.get(url=url, headers=headers)
print("response:", response.status_code)
# print("text:", response.text)

# convert response body to json and load (as dict)
response_json = response.json()
print("response_json:", response_json)
print("id:", response_json["id"])
print("self:", response_json["self"])
print("key:", response_json["key"])
# print("fields:", response_json["fields"])

issue = json.loads(response.text)
print("issue.id:", issue["id"])
print("issue.self:", issue["self"])
print("issue.key:", issue["key"])

# get sorted list of field names
fieldNames = list(issue['fields'].keys())
fieldNames.sort()
print("fieldNames:", fieldNames)

#inspect fields
for fieldName in issue['fields']:
    print("fieldName:", fieldName)
    fieldValue = issue['fields'][fieldName]
    if fieldValue:
        print(fieldName, fieldValue)


## Alternatively  access with dot notation

# turn dict into a namespace for "issue.files"
from types import SimpleNamespace
x = json.loads(response.text, object_hook=lambda x: SimpleNamespace(**x))

# get custom fields
fieldNames = list(x.fields.__dict__.keys())
custom_fields = [x for x in fieldNames if x.startswith('customfield')]

# print custom fields that are not empty
for field in custom_fields:
    fieldValue = issue['fields'][field]
    if fieldValue:
        print(field, fieldValue)

# define known (or guessed) custom fields
custom_fields_mapping = {
    "customfield_10344" : "unknown", # 9223372036854775807
    "customfield_11440" : "Automation", # Yes
    "customfield_11441" : "Test Priority", # Automation
    "customfield_11640" : "unknown", # 1|i0foo4
    "customfield_12249" : "unknown", # chrome",
    "customfield_12252" : "unknown", # Yes
    "customfield_13040" : "Cucumber Feature", # Scenario Outline
    "customfield_13240" : "Team", # UCC Commerce
    "customfield_13340" : "Product(s)" # NEJM.org
}

# list custom field names and values
for key, label in custom_fields_mapping.items():
    field = issue["fields"][key]
    print(key, label, field)

    try: 
        if type(field) is list:
            field = field[0]
        if type(field) is dict:
            value = field['value']
        if type(field) is int or type(field) is float:
            value = str(field)
        if type(field) is str:
            value = field
    except:
        print("error parsing field") 

    print(key, label, value)
    