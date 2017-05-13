from flask import Flask, request


app = Flask(__name__)


@app.route('/login', methods=["POST"])
def login():
    post = request.form
    data = ["email", "password", post]
    message = data_verification(data)
    if message:
        return message
    email, password = post["email"], post["password"]
    print(email, password)
    if user_login(email, password):
        # return empty body and if login is valid then status code OK else  Unauthorized
        return "", 200
    else:
        return "", 401


@app.route("/register", methods=["POST"])
def register():
    post = request.form
    data = ["username", "email", "password_1", "password_2", post]
    message = data_verification(data)
    if message:
        return message
    username, email, password_1, password_2 = post["username"], post["email"], post["password_1"], post["password_2"]
    print(username, email, password_1, password_2)
    if user_registration(username, email, password_1, password_2):
        return "", 200
    else:
        return "", 401


def data_verification(data):
    post = data.pop()
    if data != list(post):
        return "Input all data, please", 401
    if "email" in post:
        email = post["email"]
        if not email.endswith("@gmail.com"):
            return "Input correct email, please", 401
    if "password_1" in post:
        password_1 = post["password_1"]
        password_2 = post["password_2"]
        if password_1 != password_2:
            return "Input the same password twice", 401


def user_login(email, password):
    return True


def user_registration(username, email,  password_1, password_2):
    return True


if __name__ == "__main__":
    app.run(host="localhost", port=5000)