import os
from dotenv import load_dotenv
from jira import JIRA

# Load environment variables
load_dotenv()

JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")


def get_jira_client():
    """
    Create Jira client connection
    """
    jira = JIRA(
        server=JIRA_DOMAIN,
        basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN)
    )
    return jira


def fetch_todo_stories(project_key):
    """
    Fetch all 'To Do' stories from Jira
    """

    jira = get_jira_client()

    jql_query = f"""
    project = {project_key}
    AND status = "To Do"
    ORDER BY created ASC
    """

    issues = jira.enhanced_search_issues(jql_query)

    stories = []

    for issue in issues:

        title = issue.fields.summary

        description = issue.fields.description

        if description is None:
            description = "No description provided."

        story_text = f"""
Ticket: {issue.key}

Title: {title}

Description:
{description}
"""

        stories.append(story_text)

    return stories