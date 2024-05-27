from flask import Flask, request, jsonify
from index import algorithm
from route import Route
from environment import environment
from response import Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World!")


@app.route(Route.encrypt, methods=["POST"])
def encrypt():
    body = request.get_json()
    if "publicKey" in body and "data" in body:
        response = algorithm.encrypt(
            body["publicKey"], environment.privateKey, body["data"]
        )
        return Response.encryption(response)


@app.route(Route.decrypt, methods=["POST"])
def decrypt():
    body = request.get_json()
    if "publicKey" in body and "data" in body:
        public_key = body["publicKey"]
        response = algorithm.decrypt(public_key, environment.privateKey, body["data"])
        if response == None:
            return Response.notfound(f"{public_key} is matched with your public key")
        else:
            return Response.decryption(response)


if __name__ == "__main__":
    app.run(debug=True)
