from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def name():
    return """<!DOCTYPE html>
            <html>
                <head>
                    <title>Миссия Колонизация Марса</title>
                </head>
                <body>
                    <h1>Миссия Колонизация Марса</h1>
                </body>
            </html>"""


@app.route('/index')
def slogan():
    return """<!DOCTYPE html>
                <html>
                    <head>
                        <title>И на Марсе будут яблони цвести!</title>
                    </head>
                    <body>
                        <h1>И на Марсе будут яблони цвести!</h1>
                    </body>
                </html>"""


@app.route('/promotion')
def promotion():
    slogan = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
              "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!",
              "Присоединяйся!"]
    slogan = [f"<h1>{i}</h1>" for i in slogan]
    return f"""<!DOCTYPE html>
            <html>
            <head>
            
                <title>Слоганы</title>
            </head>
                <body>
                {"<br>".join(slogan)}
                </body>
            </html>"""


@app.route('/promotion_image')
def promotion_image():
    slogan = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
              "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!",
              "Присоединяйся!"]
    color = ['secondary', 'success', 'secondary', 'warning', 'danger']
    slogan = [f"<div class='alert alert-{color[i]} pb-3 mb-1' role='alert'>{slogan[i]}</div>" for i in range(len(slogan))]
    return f"""<!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
                    <link href="{url_for('static', filename='css/style.css')}" rel="stylesheet">
            <title>Колонизация</title>
            </head>
                <body>
                <h1>Жди нас, Марс!</h1>
                <img src="{url_for('static', filename='img/mars.png')}" alt="здесь должна была быть картинка, но не нашлась">
                {''.join(slogan)}
                </body>
            </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!DOCTYPE html>
            <html>
            <head>
                <title>Привет, Марс!</title>
            </head>
                <body>
                <h1>Жди нас, Марс!</h1>
                <img src="{url_for('static', filename='img/mars.png')}" alt="здесь должна была быть картинка, но не нашлась">
                <p>Вот она какая, красная планета.</p>
                </body>
            </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
