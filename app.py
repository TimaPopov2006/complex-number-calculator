from flask import Flask, render_template, request
import cmath  # для работы с комплексными числами
import math   # для работы с действительными числами

app = Flask(__name__)

# Данные для языков
languages = {
    "ru": {
        "title": "Квадратный корень числа",
        "input_placeholder": "Введите число, например, 2+3j",
        "submit": "Рассчитать",
        "result_label": "Результат",
        "support": "Поддержка сайта",
        "email": "Почта: tdpopov@edu.hse.ru",
    },
    "en": {
        "title": "Square Root of a Number",
        "input_placeholder": "Enter a number, e.g., 2+3j",
        "submit": "Calculate",
        "result_label": "Result",
        "support": "Site Support",
        "email": "Email: tdpopov@edu.hse.ru",
    },
    "es": {
        "title": "Raíz Cuadrada de un Número",
        "input_placeholder": "Ingrese un número, p.ej., 2+3j",
        "submit": "Calcular",
        "result_label": "Resultado",
        "support": "Soporte del sitio",
        "email": "Correo: tdpopov@edu.hse.ru",
    }
}

@app.route("/", methods=["GET", "POST"])
@app.route("/<lang>", methods=["GET", "POST"])
def index(lang="ru"):
    result = None
    language = languages.get(lang, languages["ru"])

    if request.method == "POST":
        try:
            input_value = request.form.get("number")
            # Преобразуем строку в число (комплексное или реальное)
            complex_number = complex(input_value)
            # Если число является действительным, возвращаем корень как реальное число
            if complex_number.imag == 0:
                real_number = float(input_value)
                root = math.sqrt(real_number)
                result = f"√{input_value} = +-{root}"
            else:
                root = cmath.sqrt(complex_number)
                result = f"√{input_value} = +-{root}"
        except ValueError:
            result = "Пожалуйста, введите корректное число."

    return render_template("index.html", result=result, lang=lang, language=language)

if __name__ == "__main__":
    app.run(debug=True)
