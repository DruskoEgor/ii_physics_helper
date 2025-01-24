from flask import Flask, render_template
import requests

app = Flask(__name__)

# Функция для загрузки данных из JSON
def load_formulas():
    url = "https://raw.githubusercontent.com/DruskoEgor/ii_physics_helper/main/data/data.json"  # raw-ссылка на файл
    response = requests.get(url)

    if response.status_code == 200:
        try:
            return response.json()  # Преобразуем в JSON
        except ValueError:
            raise ValueError("Не удалось распарсить JSON. Ответ от сервера: " + response.text)
    else:
        raise Exception(f"Ошибка загрузки данных: {response.status_code} - {response.text}")

@app.route('/')
def index():
    formulas = load_formulas()  # Загружаем данные из JSON
    print(formulas)
    return render_template('index.html', formulas=formulas)  # Передаем данные в шаблон

if __name__ == '__main__':
    app.run(debug=True)

