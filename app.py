from flask import Flask, render_template, request, redirect, session, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import CSRFProtect
import sqlite3
import datetime

app = Flask(__name__)
app.secret_key = "super-secret-key"
csrf = CSRFProtect(app)

app.config['SESSION_COOKIE_HTTPONLY'] = True

def admin_required():
    if session.get("role") != "admin":
        abort(403)


def get_db():
    return sqlite3.connect("auth.db")

@app.route("/admin")
def admin_panel():
    admin_required()

    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT id, username, role, failed_attempts, locked_until FROM users")
    users = cur.fetchall()

    return render_template("admin.html", users=users)

@app.route("/admin/make_admin/<int:user_id>")
def make_admin(user_id):
    admin_required()

    db = get_db()
    db.execute(
        "UPDATE users SET role='admin' WHERE id=?",
        (user_id,)
    )
    db.commit()

    return redirect("/admin")

@app.route("/admin/unlock/<int:user_id>")
def unlock_user(user_id):
    admin_required()

    db = get_db()
    db.execute(
        "UPDATE users SET failed_attempts=0, locked_until=NULL WHERE id=?",
        (user_id,)
    )
    db.commit()

    return redirect("/admin")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cur.fetchone()

        if user:
            locked_until = user[5]
            if locked_until:
                if datetime.datetime.now() < datetime.datetime.fromisoformat(locked_until):
                    return "Account locked. Try later."

            if check_password_hash(user[2], password):
                cur.execute("UPDATE users SET failed_attempts=0 WHERE id=?", (user[0],))
                db.commit()
                session["user"] = username
                session["role"] = user[3]
                return redirect("/dashboard")
            else:
                attempts = user[4] + 1
                lock_time = None
                if attempts >= 5:
                    lock_time = (datetime.datetime.now() + datetime.timedelta(minutes=15)).isoformat()
                cur.execute(
                    "UPDATE users SET failed_attempts=?, locked_until=? WHERE id=?",
                    (attempts, lock_time, user[0])
                )
                db.commit()

        return "Invalid credentials"

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (username, password) VALUES (?,?)",
                (username, password)
            )
            db.commit()
            return redirect("/")
        except:
            return "User already exists"

    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        abort(403)
    return render_template("dashboard.html", role=session["role"])

@app.route("/admin")
def admin():
    if session.get("role") != "admin":
        abort(403)
    return "Admin Panel"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
