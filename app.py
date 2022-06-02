from logging import exception
from flask import Flask,request,jsonify
from resys import GetSongs

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"

@app.route("/song",methods=['GET'])
def call():
    name = str(request.args["name"])
    try:
        getsongs = GetSongs(name)
        result = getsongs.getRecom()
        return jsonify({'result':result})
    except:
        result = "Error, Try again."
        return jsonify({'result':result})

