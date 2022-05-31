from flask import Flask,request,jsonify
from resys import GetSongs

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"

@app.route("/song",methods=['GET'])
def call():
    name = str(request.args["name"])
    getsongs = GetSongs(name)
    result = getsongs.getRecom()
    return jsonify({'result':result})


if __name__ == "__main__":
    app.run()


