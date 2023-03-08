from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=0):
    # return "<p>Hello Jose!</p>"
    return render_template('index.html', name=username, post_id=post_id)

    # Se pueden servir arvhivo completos pero Fask busca este archivo en la carpeta Templates del proyecto. CUIDADO!!


@app.route("/blog")  # Otro endpoit
def blog():
    return "<p>This are my thoughts in blogs</p>"


@app.route("/blog/2020/dogs")
def blog2():
    return "<p>This is my dog</p>"
