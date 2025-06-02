from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

EMOJI_DATA_URL = "https://raw.githubusercontent.com/cheatsnake/emojihub/refs/heads/master/emojistore/data/emojibase.json"

@app.route("/")
def index():
    try:
        response = requests.get(EMOJI_DATA_URL)
        response.raise_for_status() 
        emoji_data = response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching emoji data:", e)
        emoji_data = []

    return render_template("index.html", emojis=emoji_data)

@app.route("/emoji/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)