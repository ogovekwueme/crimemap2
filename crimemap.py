from dbhelper import DBHelper
from flask import Flask, render_template, request

app = Flask(__name__)

DB = DBHelper()

@app.route("/")
def home():
    try:
        data = DB.get_all_inputs()
    except Exception as e:
        print e
        data = None
    return render_template("home.html", data=data)

@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.form.get("userinput")
        DB.add_input(data)
    except Exception as e:
        print e
    return home()

@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print e
    return home()


if __name__ == '__main__':
    import os
    host = os.environ.get('IP','82.196.12.230')
    #port = int(os.environ.get('host','8080'))
    app.run(port=5000, debug=True,host=host)

