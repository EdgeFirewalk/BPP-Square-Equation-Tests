from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        # Проверка, не был ли введён символ (случайно или специально)
        try:
            a = float(request.form.get('a'))
            b = float(request.form.get('b'))
            c = float(request.form.get('c'))
        except ValueError:
            return render_template('char-error.html')

        # Программа работает только с полными квадратными уравнениями
        if a == 0 or b == 0 or c == 0:
            return render_template('zero-error.html')

        D = (b*b) - (4 * a * c)

        if D > 0:
            x1 = ((-b) + math.sqrt(D)) / (2 * a)
            x2 = ((-b) - math.sqrt(D)) / (2 * a)
            return render_template('two-roots.html', a=a, b=b, c=c, D=D, x1=x1, x2=x2)

        if D == 0:
            x = (-b) / (2 * a)
            return render_template('one-root.html', a=a, b=b, c=c, D=D, x=x)

        # Программа работает только с действительными корнями
        if D < 0:
            return render_template('no-roots.html', a=a, b=b, c=c, D=D)

def run():
    app.run()
