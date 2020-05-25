from flask import Flask, jsonify, json, request

pl = [
    {
        "songgg": "Do I Wanna Know?",
        "Length": "3:04",
        "artist": "Arctic Monkeys"
    },
    {
        "song": "Dance, Dance",
        "Length": "3:04",
        "artist": "Fall Out Boy"
    },
    {
        "song": "redbone",
        "Length": "4:37",
        "artist": "Childish Gambino"
    }
]

api = Flask(__name__)



@api.route('/func', methods=['GET'])
def get():
    a = jsonify(pl)
    return a


@api.route('/isalive', methods=['GET'])
def isalive():
    return "true"


@api.route('/func', methods=['PUT'])
def put():
    body = request.json
    pl.insert(0, body)
    a = jsonify(pl)
    return a


@api.route('/func', methods=['DELETE'])
def delete():
    body = request.json
    for i in range(0, len(pl)-1):
        b = pl[i]
        if body["song"] == b["song"]:
            pl.remove(pl[i])
    a = jsonify(pl)
    return a


if __name__ == "__main__":
    api.run(debug=True, port=80, host="0.0.0.0")

