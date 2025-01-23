from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

# Путь к файлу с формулами
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json')

# Загрузка данных из JSON-файла
def load_formulas():
    with open(data_path, 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route('/')
def index():
    formulas = load_formulas()  # Загружаем данные для страницы
    return render_template('index.html', formulas=formulas)

@app.route('/api/formulas')
def api_formulas():
    formulas = load_formulas()  # Загружаем данные для API
    return jsonify(formulas)

if __name__ == '__main__':
    app.run(debug=True)

