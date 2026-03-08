from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")

review_prompt = PromptTemplate.from_template("""
You are a Senior QA Engineer reviewing a software requirement.

Analyze the requirement and identify:

1. Missing acceptance criteria
2. Edge cases
3. Risks
4. Ambiguities
5. QA recommendations

Requirement:
{requirement}

Return the analysis in structured bullet points.
""")

def review_requirement(requirement):

    chain = review_prompt | llm

    response = chain.invoke({
        "requirement": requirement
    })

    return response.content