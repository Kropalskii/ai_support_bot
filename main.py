from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os, json

# Загружаем ключ из .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Инициализация клиента OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Flask-приложение
app = Flask(__name__)

# Функция поиска в FAQ
def search_faq(query):
    try:
        with open("faq.json", "r", encoding="utf-8") as f:
            faq = json.load(f)
        for item in faq:
            if item["question"].lower() in query.lower():
                return item["answer"]
    except FileNotFoundError:
        return None
    return None

# Главная страница
@app.route("/")
def index():
    return render_template("index.html")  # HTML-файл с формой

# Обработка запроса
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "")

    # Сначала ищем в FAQ
    faq_answer = search_faq(user_message)
    if faq_answer:
        return jsonify({"answer": faq_answer})

    # Если нет — спрашиваем у GPT
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты помощник службы поддержки IT-компании."},
                {"role": "user", "content": user_message}
            ]
        )
        answer = response.choices[0].message.content.strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"Ошибка при обращении к GPT: {e}"})

# Запуск сервера
if __name__ == "__main__":
    app.run(debug=True)
