from dotenv import load_dotenv
import os
import json
import csv

# Load environment variables (.env)
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Prompt template for generating structured JSON test cases
testcase_prompt = PromptTemplate.from_template("""
You are a Senior QA Engineer.

Generate 5 software test cases for the requirement below.

Return ONLY valid JSON using this format:

[
  {{
    "id": "",
    "title": "",
    "preconditions": "",
    "steps": "",
    "expected_result": "",
    "priority": ""
  }}
]

Requirement:
{requirement}
""")

# Generate test cases using AI
def generate_test_cases(requirement):

    chain = testcase_prompt | llm

    response = chain.invoke({
        "requirement": requirement
    })

    return response.content


# Save generated test cases into CSV
def save_testcases_to_csv(testcases_json, file_path):

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Clean markdown formatting if AI returns ```json
    cleaned = testcases_json.strip()

    if cleaned.startswith("```"):
        parts = cleaned.split("```")
        cleaned = parts[1] if len(parts) > 1 else cleaned

    if cleaned.startswith("json"):
        cleaned = cleaned.replace("json", "", 1)

    cleaned = cleaned.strip()

    # Convert JSON string to Python object
    data = json.loads(cleaned)

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Title",
            "Preconditions",
            "Steps",
            "Expected Result",
            "Priority"
        ])

        for tc in data:
            writer.writerow([
                tc["id"],
                tc["title"],
                tc["preconditions"],
                tc["steps"],
                tc["expected_result"],
                tc["priority"]
            ])

    return file_path