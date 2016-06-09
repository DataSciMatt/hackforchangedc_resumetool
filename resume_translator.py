#from microsofttranslator import Translator
from microsofttranslator import Translator
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
client_id = ''
secret = ''

#translator = Translator(client_id, secret)

client_id = 'jaredmerlo'
secret = 'lHHzJ1gMUAjwO8z07vTcw2IW51A31SEDdNtnticV2So='
translator = Translator(client_id, secret)

language_dict = {'Arabic' : 'ar',
'Bosnian (Latin)' : 'bs-Latn',
'Bulgarian' : 'bg',
'Catalan' : 'ca',
'Chinese Simplified' : 'zh-CHS',
'Chinese Traditional' : 'zh-CHT',
'Croatian' : 'hr',
'Czech' : 'cs',
'Danish' : 'da',
'Dutch' : 'nl',
'English' : 'en',
'Estonian' : 'et',
'Finnish' : 'fi',
'French' : 'fr',
'German' : 'de',
'Greek' : 'el',
'Haitian Creole' : 'ht',
'Hebrew' : 'he',
'Hindi' : 'hi',
'Hmong Daw' : 'mww',
'Hungarian' : 'hu',
'Indonesian' : 'id',
'Italian' : 'it',
'Japanese' : 'ja',
'Kiswahili' : 'sw',
'Klingon' : 'tlh',
'Klingon (pIqaD)' : 'tlh-Qaak',
'Korean' : 'ko',
'Latvian' : 'lv',
'Lithuanian' : 'lt',
'Malay' : 'ms',
'Maltese' : 'mt',
'Norwegian' : 'no',
'Persian' : 'fa',
'Polish' : 'pl',
'Portuguese' : 'pt',
'Queretaro Otomi' : 'otq',
'Romanian' : 'ro',
'Russian' : 'ru',
'Serbian (Cyrillic)' : 'sr-Cyrl',
'Serbian (Latin)' : 'sr-Latn',
'Slovak' : 'sk',
'Slovenian' : 'sl',
'Spanish' : 'es',
'Swedish' : 'sv',
'Thai' : 'th',
'Turkish' : 'tr',
'Ukrainian' : 'uk',
'Urdu' : 'ur',
'Vietnamese' : 'vi',
'Welsh' : 'cy',
'Yucatec Maya' : 'yua'}

def translateString(astring, lang):
    alist = astring.split(' ')
    newlist = [i['TranslatedText'] for i in translator.translate_array(alist, lang)]
    response = ' '.join(newlist)
    return response

def translate(words,language,typ='questions'):
    lang = language_dict[language]
    for key in words:
        if typ == 'questions':
            words[key] = translateString(words[key],lang)
        else:
            if key in answers_translatable:
                words[key] = translateString(words[key],lang)
    return words

questions = {'q_name' : 'Name: ',
            'q_address' : 'Address in USA: ',
            'q_phone_number' : 'Phone number: ',
            'q_email' : 'Email address: ',
            'q_objective' : 'What are you interested in?',
            'q_schooling' : 'What was your highest level of schooling?',
            'q_graduation_year' : 'When did you graduate?',
            'q_university' : 'What university did you attend?',
            'q_major' : 'What did you study?',
            'q_skills1' : 'First skill: ',
            'q_skills2' : 'Second skill: ',
            'q_skills3' : 'Third skill: '}

answers_translatable = ['q_objective','q_skills1','q_skills2','q_skills3','q_major']
questions_ordered = ['q_name',
            'q_address',
            'q_phone_number',
            'q_email',
            'q_objective',
            'q_schooling',
            'q_graduation_year',
            'q_university',
            'q_major',
            'q_skills1',
            'q_skills2',
            'q_skills3']


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/resume', methods=['GET', 'POST'])
def resume():
    answers = dict()
    for key, value in request.form.iteritems():
        answers[key] = value
    answers_translated = translate(answers, 'English',typ='answers')
    return render_template('resume.html', answers=answers)


@app.route('/build_resume', methods=['GET', 'POST'])
def build_resume():
    language = request.form['language']
    questions_translated = translate(questions,language)
    return render_template('questions.html', questions = questions_translated,questions_ordered=questions_ordered)


@app.route('/')
def translator_page():
    return render_template('landing_page.html',languages = sorted(language_dict.keys()))


if __name__ == '__main__':
    app.run(debug=False)
