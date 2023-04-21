from flask import Flask, request

app = Flask(__name__)
print('Welcome to the simple flask application...')

@app.get('/')
def index_page():
    return '<h3>Welcome to the index page ! </h3>'

@app.get('/hello')
def get_hello_world():
    return '<h2>Hello this is just an introduction'

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    return [
        {
        'name': 'Duke lester',
        'phone': '0799445562',
        'job': 'Software Engineer',
        'country': 'Kenya',
        'address': {
            'zip': 2333,
            'postal code': 62000,
            'town name': 'Kiambu, Juja',
            },
        },
        {
        'name': 'Kennedy Mongwa',
        'phone': '0799407662',
        'job': 'Software Engineer',
        'country': 'Kenya',
        'address': {
            'zip': 3400,
            'postal code': 92000,
            'town name': 'Mombasa',
            },
        },
        {
        'name': 'master man',
        'phone': '0799405562',
        'job': 'CRM Engineer',
        'country': 'Uganda',
        'address': {
            'zip': 2033,
            'postal code': 69000,
            'town name': 'Kampala',
            },
        },
        {
        'name': 'Jason Kimani',
        'phone': '079945562',
        'job': 'Software Developer',
        'country': 'Kenya',
        'address': {
            'zip': 2303,
            'postal code': 60000,
            'town name': 'Nairobi',
        },
    },
    ]

@app.route('/users/<int:user_id>')
def get_user_details(user_id: int):
    company = request.args['company']
    print('user id', user_id)
    return {
        'userId': user_id,
        'name': 'Duke lester',
        'phone': '0799445562',
        'job': 'Software Engineer',
        'country': 'Kenya',
        'address': {
            'zip': 2333,
            'postal code': 62000,
            'town name': 'Kiambu, Juja',
        },
        'company': company,
    }

@app.route('/user', methods=['POST', 'GET'])
def create_user():
    return { 'message': 'Created a Post request to create a user' }

@app.route('/add-comment', methods=["GET", "POST"])
def add_comment():
    if request.method == 'POST':
        print(request.form)
        title = request.form['title']
        body = request.form['body']
        name = request.form['name']
        return { 'title': title, 'body': body, 'name': name }
    return '''
        <form method='post'>
        <input type="text" placeholder="comment title" name="title" required/> 
        <input type="text" placeholder="comment body" name="body" required/> 
        <input type="text" placeholder="your name" name="name" required/> 
        <button>Save </button>
        </form>
    '''