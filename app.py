# app.py

import os
import subprocess
from dotenv import load_dotenv

# Load .env from the backup folder
dotenv_path = os.path.abspath("../backup_env/.env")  # Adjust if folder location differs
load_dotenv(dotenv_path)

from generators.requirement_reviewer import review_requirement
from generators.testcase_generator import generate_test_cases, save_testcases_to_csv
from generators.bdd_generator import generate_bdd_scenarios, save_bdd_to_feature_file
from generators.automation_generator import generate_playwright_script, save_automation_script
from generators.rag_pipeline import prepare_rag_pipeline  # RAG pipeline
from integrations.jira_client import fetch_todo_stories
from generators.post_generator import generate_linkedin_post, save_post_to_file
from generators.metrics_generator import calculate_metrics

def main():
    print("AI QA Assistant")
    print("--------------------------------------------------")

    # -------------------------------
    # Choose Input Type
    # -------------------------------
    print("\nChoose Input Type\n")
    print("1. Manual Requirement")
    print("2. Fetch Jira 'To Do' Stories\n")

    choice = input("Enter choice (1 or 2): ").strip()
    stories = []

    if choice == "1":
        requirement = input("\nEnter your requirement:\n")
        stories.append(f"""
Ticket: MANUAL-1

Description:
{requirement}
""")
    elif choice == "2":
        project_key = input("Enter Jira Project Key (example: SCRUM): ").upper()
        stories = fetch_todo_stories(project_key)
    else:
        print("Invalid choice. Exiting.")
        return

    # -------------------------------
    # Initialize RAG pipeline
    # -------------------------------
    try:
        vectorstore, retriever = prepare_rag_pipeline()
    except Exception as e:
        print(f"Error initializing RAG pipeline: {e}")
        retriever = None

    # -------------------------------
    # Process each story/ticket
    # -------------------------------
    for story in stories:
        lines = story.split("\n")
        ticket = "UNKNOWN"
        for line in lines:
            if "Ticket:" in line:
                ticket = line.replace("Ticket:", "").strip()

        print("\n==================================================")
        print(f"Processing Story: {ticket}")
        print("==================================================\n")
        print(story)

        ticket_folder = os.path.join("output", ticket)
        os.makedirs(ticket_folder, exist_ok=True)

        # -------------------------------
        # Requirement Review
        # -------------------------------
        print("\nRunning Requirement Review Agent...\n")
        try:
            review = review_requirement(story, retriever=retriever) if retriever else review_requirement(story)
            print(review)
        except Exception as e:
            print(f"Error during Requirement Review: {e}")

        # -------------------------------
        # Test Case Generation
        # -------------------------------
        print("\nGenerating Test Cases...\n")
        try:
            testcases = generate_test_cases(story, retriever=retriever) if retriever else generate_test_cases(story)
            csv_path = os.path.join(ticket_folder, "test_cases.csv")
            save_testcases_to_csv(testcases, csv_path)
        except Exception as e:
            print(f"Error generating test cases: {e}")

        # -------------------------------
        # BDD Scenario Generation
        # -------------------------------
        print("\nGenerating BDD Scenarios...\n")
        try:
            bdd = generate_bdd_scenarios(story, retriever=retriever) if retriever else generate_bdd_scenarios(story)
            feature_path = os.path.join(ticket_folder, "feature.feature")
            save_bdd_to_feature_file(bdd, feature_path)
        except Exception as e:
            print(f"Error generating BDD scenarios: {e}")

        # -------------------------------
        # Automation Script Generation
        # -------------------------------
        print("\nGenerating Automation Script...\n")
        try:
            script = generate_playwright_script(bdd, retriever=retriever) if retriever else generate_playwright_script(bdd)
            script_path = os.path.join(ticket_folder, "playwright_tests.py")
            save_automation_script(script, script_path)
        except Exception as e:
            print(f"Error generating automation script: {e}")

        # -------------------------------
        # Run Automation Tests + HTML Report
        # -------------------------------
        print("\nRunning Automation Tests...\n")
        report_path = os.path.join(ticket_folder, "test_report.html")
        try:
            result = subprocess.run(
                [
                    "pytest",
                    script_path,
                    f"--html={report_path}",
                    "--self-contained-html"
                ],
                capture_output=True,
                text=True
            )

            print("------ Test Execution Output ------")
            print(result.stdout)
            if result.stderr:
                print("------ Errors ------")
                print(result.stderr)

            print(f"\nHTML Test Report Generated: {report_path}")

        except Exception as e:
            print(f"Error running automation tests: {e}")

        # -------------------------------
        # Generate Advanced Metrics
        # -------------------------------
        print("\nCalculating Advanced Metrics...\n")
        try:
            metrics = calculate_metrics(ticket)
            print("Metrics Summary:", metrics)
        except Exception as e:
            print(f"Error calculating metrics: {e}")

        # -------------------------------
        # Generate LinkedIn-style Post
        # -------------------------------
        print("\nGenerating LinkedIn-style Post...\n")
        try:
            project_name = "AI-Agentic QA Assistant"
            post_text = generate_linkedin_post(ticket, project_name)
            save_post_to_file(ticket, post_text)
        except Exception as e:
            print(f"Error generating LinkedIn post: {e}")

    print("\n--------------------------------------------------")
    print("AI QA Assistant Execution Completed")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()