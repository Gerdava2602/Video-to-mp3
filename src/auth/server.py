import jwt, datetime, os
from flask import Flask, request
import sqlite3

# Connect db
conn = sqlite3.connect("auth.db", check_same_thread=False)
c = conn.cursor()

server = Flask(__name__)


@server.route("/")
def index():
    return c.execute("SELECT * FROM users").fetchall()


@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "Missing credentials", 401

    # check username and password
    c.execute(
        f"SELECT * FROM users WHERE email='{auth.username}' AND password='{auth.password}'"
    )
    user = c.fetchone()
    if not user:
        return "Invalid credentials", 401
    else:
        return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)


@server.route("/validate", methods=["POST"])
def validate():
    token = request.headers.get("Authorization")
    if not token:
        return "Missing token", 401

    encoded_jwt = token.split(" ")[1]
    try:
        decoded = jwt.decode(
            encoded_jwt, os.environ.get("JWT_SECRET"), algorithms="HS256"
        )
        return decoded, 200
    except jwt.ExpiredSignatureError:
        return "Token expired", 401
    except jwt.InvalidTokenError:
        return "Invalid token", 401


def createJWT(username, secret, auth):
    token = jwt.encode(
        {
            "user": username,
            "admin": auth,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            "iat": datetime.datetime.utcnow(),
            "admin": auth,
        },
        secret,
        algorithhm="HS256",
    )
    return token


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
