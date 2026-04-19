from ai.chains.base_chain import load_prompt
from ai.models.groq_client import generate_response

def generate_queries(resume_text: str) -> str:
    prompt_data = load_prompt("query_generation.yaml")

    template = prompt_data["template"]
    prompt = template.replace("{resume}", resume_text)

    response = generate_response(prompt)

    return response