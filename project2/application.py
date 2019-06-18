import os

from flask import Flask, session, request, render_template, redirect, url_for
from flask_socketio import SocketIO, emit

class Channel:
    def __init__(self, name):
        self.name = name
        self.messages = []

    def newMessage(self, sender, content, time):
        #deletes messages past the past 100
        while len(self.messages) > 100:
            del(self.messages[0])


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
channels = []

@app.route("/")
def index():
    return render_template("main.html")

@socketio.on("create channel")
def createChannel(data):
    channelName = data["channelname"]



if __name__ == '__main__':
    socketio.run(app)

