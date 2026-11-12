# Part 1 (front end) preview server: it only SHOWS the three pages so you can see the design.
# The real login and registration logic is added in Part 2.
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/welcome")
def welcome():
    # sample values so the welcome page has something to show
    return render_template("index.html", name="Jacob", msg="Logged in successfully")

if __name__ == "__main__":
    app.run(debug=True)
