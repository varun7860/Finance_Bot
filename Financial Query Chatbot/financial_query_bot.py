from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask  import Flask, render_template, request

app = Flask(__name__, template_folder = 'template')

financial_bot = ChatBot(name = "FinanceBot", read_only = False,
                        logic_adapters = [
                                          {
                                            'import_path': 'chatterbot.logic.MathematicalEvaluation',
                                          }

                                         ])

trainer = ChatterBotCorpusTrainer(financial_bot)

trainer.train("chatterbot.corpus.english")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(financial_bot.get_response(userText))


if __name__ == '__main__':
    app.run()
