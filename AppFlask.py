from flask import Flask, render_template
from flask_socketio import SocketIO, send
import cleaner


app = Flask(__name__)
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')

# def convert(message):
#     cleaned = leetconvert_module.leet_conver(message)
#     return cleaned

def handle_message(message):
    cleaned = cleaner.cleanText(message)
    print("Received message: " + cleaned)
    if message != "User connected":
        send(cleaned, broadcast=True)


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host="localhost")