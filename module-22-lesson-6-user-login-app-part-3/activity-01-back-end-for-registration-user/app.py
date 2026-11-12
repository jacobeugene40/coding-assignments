# User Login App - complete back end (login + logout + registration)
# The lesson stores users in a shared remote MySQL database; this version uses SQLite
# (built into Python, no server or account needed). The table is still called LoginDetails.
import os
import re
import sqlite3

from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.db")


def get_db():
    return sqlite3.connect(DB_PATH)


def init_db():
    mydb = get_db()
    mydb.execute(
        "CREATE TABLE IF NOT EXISTS LoginDetails ("
        "Id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "Name TEXT NOT NULL UNIQUE, "
        "Password TEXT NOT NULL, "
        "Email_id TEXT NOT NULL)"
    )
    mydb.commit()
    mydb.close()


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"].strip()
        password = request.form["password"]

        mydb = get_db()
        account = mydb.execute(
            "SELECT * FROM LoginDetails WHERE Name = ?", (username,)
        ).fetchone()
        mydb.close()

        # account = (Id, Name, Password, Email_id); the password is stored hashed
        if account and check_password_hash(account[2], password):
            print("login successful!")
            return render_template("index.html", msg="Logged in Successfully", name=account[1], id=account[0])
        msg = "incorrect Credentials. Kindly check"
        return render_template("login.html", msg=msg)
    return render_template("login.html")


@app.route("/logout")
def logout():
    msg = "Logged out succesfully"
    return render_template("login.html", msg=msg, name="", id="")


@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if request.method == "POST" and all(k in request.form for k in ("username", "password", "email")):
        username = request.form["username"].strip()
        password = request.form["password"]
        email = request.form["email"].strip()

        mydb = get_db()
        account = mydb.execute(
            "SELECT * FROM LoginDetails WHERE Name = ? OR Email_id = ?", (username, email)
        ).fetchone()

        if not username or not password or not email:
            msg = "Kindly fill the details!"
        elif account:
            msg = "Account already exists!"
        elif not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            msg = "Invalid email address!"
        elif not re.match(r"^[A-Za-z0-9]+$", username):
            msg = "Username must contain only characters and numbers!"
        else:
            mydb.execute(
                "INSERT INTO LoginDetails (Name, Password, Email_id) VALUES (?, ?, ?)",
                (username, generate_password_hash(password), email),
            )
            mydb.commit()
            mydb.close()
            return render_template("index.html", msg="Your Registration is Successful", name=username)
        mydb.close()
    elif request.method == "POST":
        msg = "Kindly fill the details!"
    return render_template("register.html", msg=msg)


init_db()

if __name__ == "__main__":
    app.run(debug=True)
