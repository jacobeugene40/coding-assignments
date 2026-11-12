# User Login App - Part 2: back end for login and logout
# (registration is added in Part 3, so a demo user is created here to log in with:
#  username  demo   password  demo123)
# The lesson stores users in a shared remote MySQL database; this version uses SQLite
# (built into Python, no server or account needed). The table is still called LoginDetails.
import os
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
    if not mydb.execute("SELECT 1 FROM LoginDetails WHERE Name = 'demo'").fetchone():
        mydb.execute(
            "INSERT INTO LoginDetails (Name, Password, Email_id) VALUES (?, ?, ?)",
            ("demo", generate_password_hash("demo123"), "demo@example.com"),
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


init_db()

if __name__ == "__main__":
    app.run(debug=True)
