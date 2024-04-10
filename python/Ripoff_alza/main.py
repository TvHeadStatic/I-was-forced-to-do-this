from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title = "The official unoficial Falcon fall testing...")



























if __name__ == "__main__":
    app.run(debug=True)