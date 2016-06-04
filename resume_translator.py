#from microsofttranslator import Translator
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
client_id = ''
secret = ''

#translator = Translator(client_id, secret)

def translator(word_in):
    return word_in

questions = {'q_name' : 'What is your name?',
            'q_address' : 'What is your address?'}

answers_translatable = []


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/build_resume', methods=['GET', 'POST'])
def build_resume():
    answers = dict()
    answers['a_name'] = request.form['a_name']
    answers['a_address'] = request.form['a_address']
    return render_template('resume.html', answers=answers)


@app.route('/')
def translator_page():
    for question in questions:

    return render_template('questions.html', questions = questions)


if __name__ == '__main__':
    app.run(debug=True)
