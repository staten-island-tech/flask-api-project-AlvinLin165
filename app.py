from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = 'http://ccdb.hemiola.com/characters/radicals/85?filter=gb&fields=kDefinition,kMandarin'
    data = []
    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.json()
        data = result
        print("API Response:", data)
    except (requests.RequestException, ValueError) as e:
        print("Error fetching or parsing data:", e)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)