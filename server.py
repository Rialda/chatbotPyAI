from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


#make Python speak
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
            userText = request.args.get(('msg'))
            stringResponse=str((english_bot.get_response(userText)))
            speechResponse= speak.Speak(str((english_bot.get_response(userText))))
            return {'stringResponse':stringResponse, 'speechResponse':speechResponse}


if __name__ == "__main__":
    app.run()