from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Chi Chao!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    #app.run(debug=False)
