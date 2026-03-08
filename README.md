# AI-Agentic QA Assistant

This project is the Capstone AI Academy Engineers Project from Ciklum AI Academy. It implements an AI-Agentic QA Assistant capable of reading requirements from Jira or manual input, retrieving context from TXT + PDF documents using a RAG (Retrieval-Augmented Generation) pipeline, generating test cases (CSV), BDD feature files, Playwright Python automation scripts, HTML test reports, running automation in headed browser mode for demonstration purposes, self-reflecting and reasoning based on retrieved context to ensure agentic behavior, and generating advanced metrics and a LinkedIn-style post summarizing each ticket’s automation. This project demonstrates a complete AI-Agentic pipeline combining RAG retrieval, reasoning, tool-calling, and reporting for QA automation.

## Project Structure

AI-Agentic-QA-Assistant/  
├── app.py                        # Main entrypoint  
├── generators/  
│   ├── automation_generator.py  
│   ├── rag_pipeline.py           # RAG pipeline: embeddings + vector store  
│   ├── testcase_generator.py  
│   ├── bdd_generator.py  
│   ├── requirement_reviewer.py  
│   ├── post_generator.py         # LinkedIn-style post generator  
│   └── metrics_generator.py      # Metrics generator  
├── capstone_data/  
│   └── docs/  
│       ├── requirement_doc.txt  
│       └── project_guidelines.pdf  
├── output/                        # Generated outputs per ticket  
├── venv/                          # Python virtual environment  
├── architecture.mmd               # System architecture diagram  
└── README.md  

## Dependencies

Create and activate Python virtual environment:  
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Upgrade pip and install required packages:

pip install --upgrade pip
pip install openai langchain langchain-community faiss-cpu pytest pytest-html playwright python-dotenv beautifulsoup4

Install Playwright browsers:

playwright install
Environment Variables (.env)

Create a .env file in the project root with:

OPENAI_API_KEY=your_openai_api_key_here
HEADLESS=False

Do not include your real API key in the repo.

Usage

Prepare documents in capstone_data/docs/:

requirement_doc.txt – high-level requirements and test scenarios

project_guidelines.pdf – coding guidelines, agentic behavior instructions, and output structure

Run the project:

python app.py

Choose input type:

Option	Description
1	Manual Requirement (type directly)
2	Fetch Jira "To Do" Stories (provide project key, e.g., SCRUM)

Outputs are saved in output/<ticket>/:

Output File	Description
test_cases.csv	Generated test cases
feature.feature	Generated BDD scenarios
playwright_tests.py	Playwright automation scripts
test_report.html	HTML test report from Playwright
metrics_summary.txt	Metrics: # test cases, BDD scenarios, self-healing applied
linkedin_post.txt	Automatically generated LinkedIn-style post describing the ticket and project
Execution Flow

Requirement review runs first, followed by test case and BDD scenario generation. Automation scripts are then created and executed in headed or headless browser mode. Self-healing handles minor UI changes automatically during execution. Advanced metrics are calculated and saved, and LinkedIn-style post is generated for each ticket.

Demo & Presentation Tips

Run in headed browser mode to showcase live Playwright execution. Highlight agentic reasoning and retrieval from the RAG pipeline. Show that the agent self-checks and references previous context. Use metrics and LinkedIn post to demonstrate engineering depth and communication skills. Maintain clear folder structure and ticket naming for easy review.

RAG Pipeline Overview

Text and PDF documents are loaded from capstone_data/docs/. Documents are split into chunks and converted to embeddings using OpenAI models. Embeddings are stored in a FAISS vector store. During execution, the agent retrieves relevant context before generating test cases, BDD scenarios, or automation scripts. This ensures context-aware, agentic behavior and full compliance with Capstone requirements.

Best Practices & Scoring Recommendations

Ensure modular and maintainable code. Follow coding guidelines and Playwright best practices. Keep test cases and feature files readable and mapped clearly. Generate HTML reports for each run. Demonstrate headed browser execution for demo clarity. Clear documentation (README.md + architecture.mmd) improves review scores. Proper use of RAG pipeline and reasoning ensures agentic compliance. Metrics and LinkedIn post generation showcase full engineering depth.

Architecture Diagram

See architecture.mmd for a full system overview.

References

LangChain Documentation

Playwright Python Docs

OpenAI API Docs