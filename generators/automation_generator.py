import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# -------------------------------
# Initialize LLM
# -------------------------------
llm = ChatOpenAI(model="gpt-4o-mini")

# -------------------------------
# Headed Mode + Slow Motion for demo
# -------------------------------
HEADLESS = False  # Headed mode so you can see browser
SLOW_MO = 50      # 50ms delay for visible steps

# -------------------------------
# Prompt template for automation generation
# -------------------------------
automation_prompt = PromptTemplate.from_template("""
You are a QA Automation Engineer.

Generate Playwright Python automation tests using pytest.

Application URL:
https://www.saucedemo.com/

Rules:
- Use playwright.sync_api
- Use pytest functions
- Use page.locator().is_visible() for assertions
- DO NOT pass error messages inside assertions
- Assertions must follow Playwright syntax

Example correct assertion:
assert page.locator("h3[data-test='error']").is_visible()

BDD Scenario:
{requirement}

Browser Settings:
HEADLESS = {headless}
SLOW_MO = {slow_mo}

Return ONLY valid Python code.
""")

# -------------------------------
# Generate automation script
# -------------------------------
def generate_playwright_script(requirement, retriever=None):
    """
    Converts BDD scenarios into a Python Playwright pytest automation script.
    Optionally uses retriever for agentic context.
    """
    print("\nGenerating Automation Script...\n")
    # Fill template
    filled_prompt = automation_prompt.format(
        requirement=requirement,
        headless=HEADLESS,
        slow_mo=SLOW_MO
    )

    response = llm.invoke(filled_prompt)
    script_content = response.content.strip()

    # Remove markdown formatting if AI returns ```python
    if script_content.startswith("```"):
        parts = script_content.split("```")
        script_content = parts[1] if len(parts) > 1 else script_content
    if script_content.startswith("python"):
        script_content = script_content.replace("python", "", 1)
    script_content = script_content.strip()

    return script_content

# -------------------------------
# Save automation script to file
# -------------------------------
def save_automation_script(script_content, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(script_content)
    print(f"Automation script saved to: {file_path}")
    return file_path