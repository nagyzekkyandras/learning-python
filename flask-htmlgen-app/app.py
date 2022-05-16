from flask import render_template
import flask

app = flask.Flask('my app')

if __name__ == "__main__":
    with app.app_context():
        rendered = render_template('index.html', title = "My generated page", people = [{"name": "Mark"}, {"name": "Michael"}])
    print(rendered)