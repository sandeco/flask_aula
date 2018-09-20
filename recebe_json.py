from flask import Flask, request

app = Flask(__name__)

@app.route("/json/", methods=['POST'])
def add_message():
    content = request.json
    return content

app.run(port=5000, host="0.0.0.0")
