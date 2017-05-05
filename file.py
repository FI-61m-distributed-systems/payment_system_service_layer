from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == "POST":
        return redirect(url_for('login'))
    return render_template("hello.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form['email'],
                       request.form['password']):
            return redirect(url_for('user', email=request.form['email']))
        else:
            error = "Invalid email/password"
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template("login.html", error=error)


@app.route('/<email>')
def user(email=None):
    return render_template("user.html", email=email)


def valid_login(email, password):
    return True