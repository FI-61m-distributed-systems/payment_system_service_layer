from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/login', methods=["POST"])
def login():
    # Responses to POST request
    if valid_login(request.form["email"], request.form["password"]):
        # return empty body and if login is valid then status code OK else  Unauthorized
        return "", 200
    else:
        return "", 401


def valid_login(email, password):
    return True


if __name__ == "__main__":
    app.run(host="localhost", port=5000)