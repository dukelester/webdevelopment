from flask import Flask, render_template, request

from .stories import story

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/story')
def get_story():
    return render_template('story.html')

@app.route('/form', methods=["POST", "GET"])
def get_answers():
    ''' Get the inputs from the form '''
    if request.method == 'POST':
        place = request.form['place']
        noun = request.form['noun']
        verb = request.form['verb']
        adjective = request.form['adjective']
        plural_noun = request.form['plural_noun']
        result_story = story.generate({
            'place': place, 'noun': noun,
            'verb': verb, 'adjective': adjective,
            'plural_noun': plural_noun,
        })
        return render_template('story.html', story=result_story)
    return render_template('form.html')
