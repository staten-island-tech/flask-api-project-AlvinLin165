from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():

    url = 'http://ccdb.hemiola.com/characters/radicals/85?filter=gb&fields=kDefinition,kMandarin'
    print("API Response:", data)  # <--- Add this line
    response = requests.get(url)

    try:
        data = response.json()
    except ValueError:
        data = []

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)