from flask import Flask, Response, request, render_template
from app import stream_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream", methods=["POST"])
def stream():
    message = request.json['message']

    def generate():
        for chunk in stream_response(message):
            yield chunk

    return Response(generate(), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True, port=5001)