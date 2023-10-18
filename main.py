from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': '11',
        'name': 'dd',
    },
    {
        'author': '23',
        'name': 'ertu',
    },
    {
        'author': '55',
        'name': 'fgh',
    }
]


@app.route('/home')
@app.route('/')
def hello():
    return render_template('home.html', title='home', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
