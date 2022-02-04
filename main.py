from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    print (request.headers)
    return "Hello World!"

@app.route("/best_song")
def GetBestSongEver():
    return "Never gonna give you up"

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')