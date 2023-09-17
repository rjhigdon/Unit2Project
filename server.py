from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cupcakes")
def cupcakes():
    return render_template("cupcakes.html")

@app.route("/one_cake")
def one_cake():
    return render_template("one_cake.html")

@app.route("/order")
def order():
    return render_template("order.html")



if __name__ == "__main__":
    app.run(debug = True, port = 8000, host = "localhost")


#run this file to start server