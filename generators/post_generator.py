# generators/post_generator.py
import os
from openai import OpenAI

# Load API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_linkedin_post(ticket_id: str, project_name: str) -> str:
    """
    Generate a LinkedIn-style post about the AI Agentic QA Assistant for a given ticket.
    """
    prompt = f"""
    Write a professional, concise LinkedIn post (~100 words) about our AI Agentic QA Assistant.
    Highlight that it:
    - Reads Jira or manual requirements
    - Uses RAG pipeline for context
    - Generates test cases, BDD scenarios, and automation scripts
    - Runs automation with self-healing
    Mention the ticket ID: {ticket_id} and project name: {project_name}.
    Make it engaging and suitable for LinkedIn.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )

    post_text = response.choices[0].message.content.strip()
    return post_text

def save_post_to_file(ticket_id: str, post_text: str):
    """
    Save the generated post under output/<ticket>/linkedin_post.txt
    """
    output_dir = os.path.join("output", ticket_id)
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "linkedin_post.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(post_text)
    print(f"LinkedIn post saved to: {file_path}")