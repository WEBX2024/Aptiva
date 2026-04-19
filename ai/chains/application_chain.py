from ai.chains.base_chain import load_prompt
from ai.models.groq_client import generate_response


def generate_answer(resume_text: str, question: str) -> str:
    prompt_data = load_prompt("application_assistant.yaml")

    template = prompt_data["template"]

    prompt = template.replace("{resume}", resume_text)
    prompt = prompt.replace("{question}", question)

    response = generate_response(prompt)

    return response