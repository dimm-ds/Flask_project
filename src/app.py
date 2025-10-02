from flask import Flask

# Создаем объект приложения Flask
app = Flask(__name__)


# Определяем маршрут и привязываем его к функции
@app.route("/hello")
def about():
    return "Hello, world!"


@app.route("/info")
def info():
    return "This is an informational page."


@app.route("/calc/<a>/<b>")
def calc(a, b):
    try:
        float(a)
        float(b)
    except ValueError:
        return "Неправильный формат ввода"
    return f"The sum of {a} and {b} is {a + b}."


@app.route("/reverse/", defaults={'word': ''})
@app.route("/reverse/<word>")
def reverse(word):
    if not word:
        return 'Нет слова для переворота'

    return f'{word}'[::-1]


@app.route("/user/<name>/<age>")
def user(name, age):
    if not age > 0:
        return 'Некорректный возраст'
    return f"Hello, {name}. You are {age} years old."






# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
