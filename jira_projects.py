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
parser.add_argument('-t', '--token', required=False, help="Jira personal access token; optional (or set environment variable JIRA_TOKEN)")
args = parser.parse_args()
print("args:", args)

# get parameters
JIRA_TOKEN = args.token or os.getenv("JIRA_TOKEN")
print("JIRA_TOKEN:", JIRA_TOKEN)
if not JIRA_TOKEN:
    print("JIRA_TOKEN must be set")
    exit()

# URL info
JIRA_BASE_URL = "https://jira.mms.org"
JIRA_API_PATH = "rest/api/latest"
# ZEPHYR_API_PATH = "rest/zapi/latest"

PROJECT_ENDPOINT = "project"

# build url
url = f"{JIRA_BASE_URL}/{JIRA_API_PATH}/{PROJECT_ENDPOINT}"
print("url:", url)

# add authorization header
headers = {}
headers["Authorization"] =  f"Bearer {JIRA_TOKEN}"
print("headers:", headers)

response = requests.get(url=url, headers=headers)
print("response", response.status_code)
print(response.text)

projects = response.json()
for project in projects:
	print("Project: ", project)
	print()
	# print(json.dumps(project))
	print(project["self"], project["key"], project["name"],  "projectType=", project["projectTypeKey"], "archived=", project["archived"] )
	

	if "projectCategory" in project:

		projectCategory = project["projectCategory"]
		if projectCategory:
			print("projectCategory=", projectCategory["name"], "\t", projectCategory["description"])

	print()