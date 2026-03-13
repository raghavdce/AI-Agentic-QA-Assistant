# AI-Agentic QA Assistant

This project is the Capstone AI Academy Engineers Project from Ciklum AI Academy. It implements an AI-Agentic QA Assistant capable of reading requirements from Jira or manual input, retrieving context from TXT + PDF documents using a RAG (Retrieval-Augmented Generation) pipeline, generating test cases (CSV), BDD feature files, Playwright Python automation scripts, HTML test reports, running automation in headed browser mode for demonstration purposes, self-reflecting and reasoning based on retrieved context to ensure agentic behavior, and generating advanced metrics and a LinkedIn-style post summarizing each ticket’s automation. This project demonstrates a complete AI-Agentic pipeline combining RAG retrieval, reasoning, tool-calling, and reporting for QA automation.

## Objectives
• Demonstrate an AI-Agentic QA workflow
• Apply RAG-based context retrieval for requirement understanding
• Automatically generate QA artifacts (test cases, BDD, automation)
• Perform AI self-reflection and reasoning
• Produce engineering metrics and automated reporting
• Demonstrate an AI-agentic QA workflow with automated test generation and execution

## Key Features

• AI-agentic QA workflow
• RAG-based requirement understanding
• Automatic test case generation
• BDD scenario generation
• Playwright automation script generation
• Self-reflection and requirement validation
• Automated metrics generation
• LinkedIn-style reporting
• CI-ready automation execution

## Project Structure

AI-Agentic-QA-Assistant/  
├── app.py                        # Main entrypoint 
├── agents   
    ├── qa_agent.py                        
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

## Module Descriptions

- **qa_agent.py** – Coordinates the overall AI QA workflow, invoking reasoning, tool-calling, and self-reflection loops. Acts as the central agent controlling test case generation, BDD, automation, and evaluation.

- **automation_generator.py** – Generates Playwright automation scripts from BDD scenarios or test cases. Supports optional self-healing for minor UI changes during execution.

- **bdd_generator.py** – Converts user stories or requirements into Gherkin-style BDD scenarios. Ensures edge cases, negative cases, and acceptance criteria are included.

- **data_loader.py** – Loads and preprocesses text, PDF, and Word documents for the RAG pipeline. Handles chunking, encoding, and prepares documents for embeddings.

- **metrics_generator.py** – Calculates advanced metrics such as number of test cases, BDD scenarios, coverage, and self-healing applied. Provides a quantitative evaluation of automation outputs.

- **post_generator.py** – Creates a LinkedIn-style post summarizing the AI-generated outputs and project impact. Automates professional communication about each ticket or feature.

- **rag_pipeline.py** – Implements Retrieval-Augmented Generation: splits documents, creates vector embeddings, stores embeddings in ChromaDB vector database, and retrieves relevant context. Enables context-aware reasoning for test generation.

- **requirement_reviewer.py** – Analyzes Jira stories or manual requirements for gaps, risks, and missing validations. Acts as the AI “senior QA” reviewing completeness and compliance.

- **testcase_generator.py** – Generates structured test cases (CSV) from stories or retrieved context. Ensures coverage of edge cases and acceptance criteria.

- **app.py** – Main entrypoint for the project; handles user input, initializes RAG pipeline, invokes agents, and saves outputs. Coordinates the full pipeline from requirement input to automation execution.

## Dependencies

Create and activate Python virtual environment:  

python -m venv venv

## Windows
venv\Scripts\activate

## macOS/Linux
source venv/bin/activate

## Upgrade pip and install required packages:

pip install --upgrade pip
pip install openai langchain langchain-community chromadb pytest pytest-html playwright python-dotenv beautifulsoup4

## Install Playwright browsers:

playwright install
Environment Variables (.env)

## Create a .env file in the project root with:

OPENAI_API_KEY=your_openai_api_key_here
HEADLESS=False

Do not include your real API key in the repo.

## Usage

Prepare documents in capstone_data/docs/:

requirement_doc.txt – high-level requirements and test scenarios

project_guidelines.pdf – coding guidelines, agentic behavior instructions, and output structure

## Run the project:

python app.py

## Choose input type:

Option	Description
1	Manual Requirement (type directly)
2	Fetch Jira "To Do" Stories (provide project key, e.g., SCRUM)

## Outputs are saved in output/<ticket>/:

Output File	Description
test_cases.csv	Generated test cases
feature.feature	Generated BDD scenarios
playwright_tests.py	Playwright automation scripts
test_report.html	HTML test report from Playwright
metrics_summary.txt	Metrics: # test cases, BDD scenarios, self-healing applied
linkedin_post.txt	Automatically generated LinkedIn-style post describing the ticket and project
Execution Flow

Requirement review runs first, followed by test case and BDD scenario generation. Automation scripts are then created and executed in headed or headless browser mode. Self-healing handles minor UI changes automatically during execution. Advanced metrics are calculated and saved, and LinkedIn-style post is generated for each ticket.

## RAG Pipeline Overview

Text and PDF documents are loaded from capstone_data/docs/. Documents are split into chunks and converted to embeddings using OpenAI models. Embeddings are stored in a ChromaDB vector database. During execution, the agent retrieves relevant context before generating test cases, BDD scenarios, or automation scripts. This ensures context-aware, agentic behavior and full compliance with Capstone requirements.

## RAG Pipeline Snippet

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    docs_split,
    embeddings,
    persist_directory="./chroma_db"
)

retriever = vectorstore.as_retriever(search_kwargs={"k":3})

## Best Practices & Scoring Recommendations

Ensure modular and maintainable code. Follow coding guidelines and Playwright best practices. Keep test cases and feature files readable and mapped clearly. Generate HTML reports for each run. Demonstrate headed browser execution for demo clarity. Clear documentation (README.md + architecture.mmd) improves review scores. Proper use of RAG pipeline and reasoning ensures agentic compliance. Metrics and LinkedIn post generation showcase full engineering depth.

## Architecture Diagram

```mermaid
flowchart TD
A[User Input] -->|Manual / Jira| B[Requirement Review Module]
B --> C[RAG Pipeline (Context Retrieval)]
C --> D[Test Case Generator]
C --> E[BDD Generator]
C --> F[Automation Script Generator]
D --> G[CSV Test Case Output]
E --> H[Feature File Output]
F --> I[Playwright Script Output]
F --> J[Run Automation (Headed/Headless)]
J --> K[HTML Test Report]
J --> L[Self-Healing Mechanism]
L --> F
K --> M[Evaluation / Metrics]

## System Architecture Explanation

The system follows an AI-agentic pipeline:

User Input → Preprocessing → RAG Retrieval → Reasoning Agent → Self-Reflection → Tool Calling → Outputs

User input is provided through Jira stories or manual requirements. 
The RAG layer retrieves relevant context using vector similarity search. 
The reasoning agent analyzes requirements and generates QA artifacts. 
A self-reflection stage evaluates completeness and coverage. 
Finally, tool-calling modules generate automation scripts, reports, metrics, and GitHub outputs.

## References

LangChain Documentation  
https://python.langchain.com/

Playwright Python Docs  
https://playwright.dev/python/

OpenAI API Docs  
https://platform.openai.com/docs/