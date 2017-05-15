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
        return response_ok("")
    else:
        return response_error("")


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
        return response_ok("")
    else:
        return response_error("")


def data_verification(data):
    post = data.pop()
    if data != list(post):
        return response_error("Input all data, please")
    if "email" in post:
        email = post["email"]
        if not email.endswith("@gmail.com"):
            return response_error("Input correct email, please")
    if "password_1" in post:
        password_1 = post["password_1"]
        password_2 = post["password_2"]
        if password_1 != password_2:
            return response_error("Input the same password twice")


def response_ok(message):
    return message, 200


def response_error(message):
    return message, 401


def user_login(email, password):
    return True


def user_registration(username, email,  password_1, password_2):
    return True


if __name__ == "__main__":
    app.run(host="localhost", port=5000)