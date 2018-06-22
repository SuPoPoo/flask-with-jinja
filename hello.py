from flask import Flask,render_templates,url_for

myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__hello__":
    myapp.run(debug = True)

