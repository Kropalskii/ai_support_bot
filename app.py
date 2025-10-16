from flask import Flask, request, jsonify, render_template_string
from ai_utils import smart_answer

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
  <title>AI Support</title>
</head>
<body style="font-family: sans-serif; max-width:600px; margin:50px auto;">
  <h2>💬 AI Support Bot</h2>
  <form onsubmit="send(event)">
    <input id="q" placeholder="Введите вопрос..." style="width:400px;">
    <button>Спросить</button>
  </form>
  <pre id="out"></pre>
  <script>
  async function send(e){
    e.preventDefault();
    const q = document.getElementById('q').value;
    const res = await fetch('/ask', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({message:q})
    });
    const data = await res.json();
    document.getElementById('out').textContent = data.answer || data.error;
  }
  </script>
</body>
</html>
"""

@app.get("/")
def home():
    return render_template_string(HTML)

@app.post("/ask")
def ask():
    data = request.get_json(force=True)
    message = (data or {}).get("message", "").strip()
    if not message:
        return jsonify(error="Введите вопрос!"), 400
    try:
        answer = smart_answer(message)
        return jsonify(answer=answer)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
