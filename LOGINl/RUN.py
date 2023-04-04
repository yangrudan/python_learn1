from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('modl.html')


if __name__ == '__main__':
    app.run(port=5050, debug=True)