import os
import sys
import json
import requests

class JiraRequest(object):

    JIRA_BASE_URL = "https://jira.mms.org"
    JIRA_API_PATH = "rest/api/latest"
    
    CUSTOM_FIELDS = {
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

    def __init__(self, **kwargs):

        self.JIRA_BASE_URL = kwargs.get("JIRA_BASE_URL") or os.getenv("JIRA_BASE_URL") or JiraRequest.JIRA_BASE_URL
        self.JIRA_API_PATH = kwargs.get("JIRA_API_PATH") or os.getenv("JIRA_API_PATH") or JiraRequest.JIRA_API_PATH

    @property
    def JIRA_URL(self):
        return f"{self.JIRA_BASE_URL}/{self.JIRA_API_PATH}"
    
if __name__ == "__main__":
    import main
    args = main.parse_args(sys.argv)
    print(args)
    jira = JiraRequest(**vars(args))

    print("JIRA_URL:", jira.JIRA_URL)