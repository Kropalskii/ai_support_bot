AI Support Bot — Flask + OpenAI

Интеллектуальный ассистент поддержки, объединяющий FAQ-поиск и возможности GPT-модели.
Проект написан на Python (Flask) с интеграцией OpenAI API и локальной базой часто задаваемых вопросов.

                          --Функциональность--

Отвечает на вопросы из локального faq.json;

При отсутствии совпадений — использует OpenAI GPT для генерации ответа;

Веб-интерфейс на Flask с формой общения;

Легко расширяется и адаптируется под бизнес-нужды.

                          --Чтобы запустить--
# 1. Клонируем репозиторий
git clone https://github.com/Kropalskii/ai_support_bot.git
cd ai_support_bot

# 2. Создаем виртуальное окружение
python -m venv venv
source venv/bin/activate       # (Linux/macOS)
venv\Scripts\activate          # (Windows)

# 3. Устанавливаем зависимости
pip install -r requirements.txt

# 4. Добавляем в корень файл .env с содержимым:
OPENAI_API_KEY=your_api_key_here

# 5. Запускаем Flask
python main.py


                              --Технологии--

Python 3.10+

Flask

OpenAI API

dotenv

JSON
