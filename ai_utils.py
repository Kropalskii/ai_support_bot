import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT = "Ты дружелюбный и лаконичный помощник службы поддержки."

def search_faq(query: str, path="faq.json") -> str | None:
    """Проверяет, есть ли ответ в локальном FAQ."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            faq = json.load(f)
        query = query.lower()
        for item in faq:
            if item["question"].lower() in query:
                return item["answer"]
    except Exception:
        pass
    return None

def ask_gpt(prompt: str) -> str:
    """Отправляет вопрос в OpenAI API."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        max_tokens=250,
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()

def smart_answer(query: str) -> str:
    """Сначала ищет в FAQ, потом спрашивает у GPT."""
    faq_answer = search_faq(query)
    if faq_answer:
        return faq_answer
    return ask_gpt(query)
