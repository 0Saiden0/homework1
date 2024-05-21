from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shoes/')
def html_shoes():
    return render_template('shoes.html')

@app.route('/jackets/')
def html_jackets():
    return render_template('jackets.html')

if __name__ == '__main__':
    app.run(debug=True)