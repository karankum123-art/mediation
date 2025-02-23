from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Meditation and Self-Care Exercises
meditation_tips = [
    "5-minute deep breathing exercise",
    "Guided meditation for relaxation",
    "Body scan meditation for stress relief",
    "Mindfulness walk for 10 minutes",
    "Gratitude journaling for 5 minutes"
]

self_care_tips = [
    "Take a warm bath with relaxing music",
    "Practice yoga for 10 minutes",
    "Read a book for mental relaxation",
    "Listen to calming music",
    "Try progressive muscle relaxation"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    
    if "meditation" in user_input:
        response = random.choice(meditation_tips)
    elif "self-care" in user_input or "relax" in user_input:
        response = random.choice(self_care_tips)
    else:
        response = "I can suggest meditation and self-care exercises. Try asking: 'Suggest a meditation' or 'Give me a self-care tip'."
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
