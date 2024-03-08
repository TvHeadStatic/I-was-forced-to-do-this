from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title = "flask")


@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    return render_template("calculator.html", title = "Calculator Theory")

@app.route("/:3", methods=['GET', 'POST'])
def jun():
    match (request.method):
        case 'GET':
            return "wth"
        case 'POST':
            return "{}".format(request.form["Bruv"])

if __name__ == "__main__":
    app.run(debug=True)