from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title = "Falcon fall co.")

@app.route("/products")
def index():
    return render_template("index.html", title = "Falcon fall co.")




























if __name__ == "__main__":
    app.run(debug=True)