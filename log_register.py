from flask import Flask, request
import sys

app = Flask(__name__)


@app.route('/login', methods=["POST"])
def login():
    post = request.form
    expected_labels = ["email", "password"]
    if data_error(post, expected_labels):
        return response_client_error("Input all data, please")
    email, password = post["email"], post["password"]
    if email_error(email):
        return response_client_error("Input correct email, please")

    if user_login(email, password):
        # return empty body and if login is valid then status code OK else  Unauthorized
        return response_ok("")
    else:
        return response_client_error("")


@app.route("/register", methods=["POST"])
def register():
    post = request.form
    expected_labels = ["username", "email", "password_1", "password_2"]
    if data_error(post, expected_labels):
        return response_client_error("Input all data, please")
    username, email, password_1, password_2 = post["username"], post["email"], post["password_1"], post["password_2"]
    if email_error(email):
        return response_client_error("Input correct email, please")
    if password_error(password_1, password_2):
        return response_client_error("Input the same password twice, please")

    if user_registration(username, email, password_1, password_2):
        return response_ok("")
    else:
        return response_server_error("")


def data_error(data, labels):
    if labels != list(data):
        return True
    return False


def email_error(email):
    email = email.split("@")
    allowed_emails = ["gmail.com", "yandex.ru", "mail.ru"]
    if len(email) != 2:
        return True
    email = email[1]
    if email not in allowed_emails:
        return True
    return False


def password_error(password_1, password_2):
    if password_1 != password_2:
        return True
    return False


def response_ok(message):
    return message, 200


def response_client_error(message):
    return message, 401


def response_server_error(message):
    return message, 500


def user_login(email, password):
    return True


def user_registration(username, email,  password_1, password_2):
    return True

if __name__ == "__main__":
    app.run(host=sys.argv[1], port=sys.argv[2])

