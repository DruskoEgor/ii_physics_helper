import os
import json
import requests
from flask import Flask, render_template

app = Flask(__name__)

# Прямой URL для файла на GitHub
GITHUB_JSON_URL = 'https://raw.githubusercontent.com/DruskoEgor/ii_physics_helper/main/data/data.json'

# Кэшируем данные при старте приложения
def load_formulas():
    response = requests.get(GITHUB_JSON_URL)
    return response.json()

# Загружаем данные при старте
formulas = load_formulas()

@app.route('/')
def index():
    return render_template('index.html', formulas=formulas)

if __name__ == '__main__':
    app.run(debug=True)
