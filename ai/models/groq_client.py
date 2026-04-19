from groq import Groq
from infra.settings import settings
from ai.config import AIConfig

client = Groq(api_key=settings.GROQ_API_KEY)


def generate_response(prompt: str) -> str:
    models = AIConfig.GROQ_MODELS

    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content

        except Exception as e:
            print(f"Model {model} failed: {e}")

    raise Exception("All models failed")