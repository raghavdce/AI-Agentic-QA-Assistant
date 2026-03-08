from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Prompt template for BDD generation
bdd_prompt = PromptTemplate.from_template("""
You are a QA automation expert.

Convert the requirement below into BDD scenarios using Gherkin syntax.

Requirement:
{requirement}

Return ONLY the Gherkin feature content.
""")


# Generate BDD scenarios
def generate_bdd_scenarios(requirement):

    chain = bdd_prompt | llm

    response = chain.invoke({
        "requirement": requirement
    })

    return response.content


# Save BDD into .feature file
def save_bdd_to_feature_file(bdd_content, file_path):

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    cleaned = bdd_content.strip()

    # Remove markdown formatting if AI returns ```gherkin
    if cleaned.startswith("```"):
        parts = cleaned.split("```")
        cleaned = parts[1] if len(parts) > 1 else cleaned

    if cleaned.startswith("gherkin"):
        cleaned = cleaned.replace("gherkin", "", 1)

    cleaned = cleaned.strip()

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(cleaned)

    print(f"BDD feature file saved to: {file_path}")

    return file_path