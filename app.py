from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🎉 Python Flask App deployed to Azure Web App via GitHub Actions!"

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}, welcome to Azure Web App!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
