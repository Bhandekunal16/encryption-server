from flask import jsonify


class Response:
    def encryption(data):
        return (
            jsonify(
                {"encrypted": data, "status": True, "statusCode": 200, "msg": "success"}
            ),
            200,
        )

    def decryption(data):
        return (
            jsonify(
                {"decrypted": data, "status": True, "statusCode": 200, "msg": "success"}
            ),
            200,
        )

    def notfound(data):
        return (
            jsonify(
                {
                    "encrypted": data,
                    "status": False,
                    "statusCode": 404,
                    "msg": "not found",
                }
            ),
            404,
        )

    def custom(value):
        print(value)
        return value
