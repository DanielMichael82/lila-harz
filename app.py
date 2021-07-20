import os
import json
from flask import (
    Flask, flash, render_template,
    request)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    data = []
    with open("data/lilaharz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", lilaharz=data)


@app.route("/collections")
def collections():
    data = []
    with open("data/products.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("collections.html", products=data)

@app.route("/collections/<product_name>")
def about_product(product_name):
    product = {}
    with open("data/products.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == product_name:
                product = obj
    return render_template("products.html", product=product)


@app.route("/care_guide")
def care_guide():
    return render_template("care_guide.html", page_title="Care Guide")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank you {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/login")
def login():
    return render_template("login.html", page_title="Login")


@app.route("/coasters")
def coasters():
    return render_template("coasters.html", page_title="Coasters")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
