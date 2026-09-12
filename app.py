from flask import Flask, render_template

app = Flask(__name__, static_folder='templates')


@app.route("/")
def Main():
    return render_template("MainPage.html")


@app.route("/catalog")
def catalog():
    return render_template("catalog.html")

@app.route("/contacs")
def contacs():
    return render_template("contacs.html")

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)

