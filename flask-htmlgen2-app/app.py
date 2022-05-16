from flask import render_template
import flask

app = flask.Flask('my app')

renderelesimappa = "public"

def renderelesfileba(fajlneve, cim):
    fajlneve = renderelesimappa + "/" + fajlneve
    rendered = render_template("index.html", title = cim, people = [{"name": "Mark"}, {"name": "Michael"}])
    file=open(fajlneve, "w")
    file.write(rendered)
    file.close()

if __name__ == "__main__":
    with app.app_context():
#        rendered = render_template('index.html', title = "My generated page", people = [{"name": "Mark"}, {"name": "Michael"}])
        renderelesfileba("index.html", "Főoldal")
        renderelesfileba("contact.html", "Kapcsolat")
        renderelesfileba("about.html", "Rólunk")
    print("A futás sikeres")