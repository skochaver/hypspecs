from flask import Flask, render_template

app = Flask(__name__)
debug = True

@app.route('/')
def intro_page():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=debug)
