import nltk
from nltk.chat.util import Chat, reflections
from flask  import Flask, render_template, request

app = Flask(__name__, template_folder = 'template')

class FinanceBot(object):

    def __init__(self):

        self.bot = None
        self.response = ''

        self.reflections = {'i am': 'your are',
                            'i was': 'you were',
                            'i': 'you',
                            "i'm": 'you are',
                            "i'd": 'you would',
                            "i've": 'you have',
                            "i'll": 'you will',
                            'my': 'your',
                            'you are': 'I am',
                            'you were': 'I was',
                            "you've": 'I have',
                            "you'll": 'I will',
                            'your': 'my',
                            'yours': 'mine',
                            'you': 'me',
                            'me': 'you'}

        self.responses = [
                           [
                             r"hi|hey|hello",
                             ["Hello! please enter your name"]
                           ],

                           [
                             r"rajesh|Rajesh",
                             ["Enter your age"]
                           ],

                           [
                             r"21",
                             ["Enter your acc number"]
                           ],

                           [
                             r"123637362936",
                             ["Enter your average monthly stipend"]
                           ],

                           [
                             r"10000",
                             ["Enter your average salary per month"]
                           ],

                           [
                             r"20000",
                             ["Do you Invest in Stocks?"]
                           ],
                           

                           [
                             r"No|no|no i don't",
                             ["Do you want to know what's a stock market?"]
                           ],
                           

                           [
                             r"yes|Yes|yes i want to know",
                             ["Stock market is a place where buyers and \
                               sellers trade stocks which is the ownership \
                               claims on buisnesses.They may either be public \
                               private."]
                           ],
                           

                           [
                             r"Ok|Thank you|Fine|fine|ok",
                             ["Do you want to learn more on stock market?"]
                           ],
                           

                           [
                             r"yeah i want to know more|yeah want to know",
                             ["visit investopedia.com to know more"]
                           ],

                           
                           [
                             r"Latest news on finance|latest news on finance",
                             ["Seuz canal accident amy cause huge looses in \
                               money and also lives, says world Bank CEO."]
                           ],

                          ]

    def train(self):

        self.bot = Chat(self.responses, self.reflections)

        print("Training Completed")
            

    def get_response(self,user_text):

        self.response = self.bot.respond(user_text)

        return self.response
                        

finance_bot = FinanceBot()

finance_bot.train()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(finance_bot.get_response(userText))

if __name__ == '__main__':
    app.run()
                           

                           

        
