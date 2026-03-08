from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini")


review_prompt = PromptTemplate.from_template("""
You are a Senior QA Architect.

Review the requirement below and identify:

1. Missing Acceptance Criteria
2. Edge Cases
3. Risks
4. Ambiguities
5. QA Recommendations

Requirement:
{requirement}
""")


def review_requirement(requirement):

    chain = review_prompt | llm

    response = chain.invoke({
        "requirement": requirement
    })

    return response.content