import os
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
    return render_template("sign_up.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
