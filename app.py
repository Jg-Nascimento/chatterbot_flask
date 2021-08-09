#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
#create chatbot
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
'''
englishBbot = ChatBot("Chatterbot", 
                     storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     database = mongodb_name,
                     database_uri = mongodb_uri)
'''
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train('chatterbot.corpus.portuguese') #train the chatter bot for pt-br

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))

if __name__ == "__main__":
    app.run()
