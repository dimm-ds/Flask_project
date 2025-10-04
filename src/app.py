from flask import Flask

# Создаем объект приложения Flask
app = Flask(__name__)


# Определяем маршрут и привязываем его к функции
@app.route("/hello")
def hello():
    return "Hello, world!"


@app.route("/info")
def info():
    return "This is an informational page."


@app.route("/calc/<int:a>/<int:b>")
def calc(a, b):
    return f"The sum of {a} and {b} is {a + b}."


@app.route("/reverse/<word>")
def reverse(word=''):
    if not word:
        return 'No word to reverse', 400
    return word[::-1]


@app.route("/user/<name>/<int:age>")
def user(name, age):
    if age <= 0:
        return 'Invalid age', 400
    return f"Hello, {name}. You are {age} years old."






# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
