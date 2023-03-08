import os
import sys
import argparse

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL") or "https://jira.mms.org/rest/api/latest"
JIRA_TOKEN = os.getenv("JIRA_TOKEN")

def mask(s, unmask=4):
    return len(s[:-unmask])*"*"+s[-unmask:]

def env_or_required(key, default=None):
    value = os.getenv(key) or default
    if value: 
        return {'default': value}
    else:
        return {'required': True}

def parse_args(argv):
    # configure arguments

    # use argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', **env_or_required("JIRA_BASE_URL", JIRA_BASE_URL), help="Jira base URL (or environment variable JIRA_BASE_URL)")
    parser.add_argument('-t', '--token', **env_or_required("JIRA_TOKEN"), help="Jira personal access token (or environment variable JIRA_TOKEN)")
    parser.add_argument('-p', '--project', help="Jira project key (e.g. QAUTO)")
    parser.add_argument('-i', '--issue', help="Jira issue key (e.g. QAUTO-1234)")
    args = parser.parse_args()

    print("args:", args)
    print("project:", args.project)
    print("issue:", args.issue)
    print("url: ", args.url)
    print("token: ", mask(args.token))

if __name__ == "__main__":
    print("running main")
    args = parse_args(sys.argv)
