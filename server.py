from flask import Flask, render_template
from cupcakes import get_cupcakes, add_cupcake_dictionary, find_cupcake


app = Flask(__name__)

    
@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("sample.csv"))

@app.route("/cupcakes")
def cupcakes():
    return render_template("cupcakes.html")

@app.route("/find_cake")
def find_cake():
    return render_template("find_cake.html")

@app.route("/order")
def order():
    return render_template("order.html")

if __name__ == "__main__":
    app.run(debug = True, port = 8000, host = "localhost")


#run this file to start server but only after you start a  venv
