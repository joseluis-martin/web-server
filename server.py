from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return "<p>Hello Jose!</p>"
    return render_template('index.html')
    # Se pueden servir archivo completos pero Fask busca este archivo en la carpeta Templates del proyecto. CUIDADO!!

@app.route('/<string:page_name>')
def index(page_name):
    # return "<p>Hello Jose!</p>"
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter = ',', quotechar = '|', quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return ('sth went wrong')




""" @app.route('/index.html')
def index():
    # return "<p>Hello Jose!</p>"
    return render_template('index.html')

@app.route('/about.html')
def about():
    # return "<p>Hello Jose!</p>"
    return render_template('about.html')

@app.route('/works.html')
def works():
    # return "<p>Hello Jose!</p>"
    return render_template('works.html')

@app.route('/work.html')
def work():
    # return "<p>Hello Jose!</p>"
    return render_template('work.html')

@app.route('/contact.html')
def contact():
    # return "<p>Hello Jose!</p>"
    return render_template('contact.html') """
