from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title = "Flesk")


@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    equals =  0
    match(request.method):
        case 'GET':
            if request.args.get('1stInput') != None and request.args.get("2ndInput") != None:
                z = float(request.args.get('1stInput'))
                y = float(request.args.get("2ndInput"))
                match(request.args.get("operation")):
                    case "-":  
                        equals = z - y
                    case "*":
                        equals = z * y
                    case "/": 
                        if y == 0 :
                            equals = None
                        else:
                            equals = z / y 
                    case _:
                        equals = z + y 
    return render_template("calculator.html", title = "Kálkůlátór", uwu = equals)


@app.route("/:3", methods=['GET', 'POST'])
def jun():
    match (request.method):
        case 'GET':
            return "wth"
        case 'POST':
            return "{}".format(request.form["Bruv"])

if __name__ == "__main__":
    app.run(debug=True)