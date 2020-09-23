import re
from flask import Flask, request
import telegram
from bot_telegram.credentials import bot_token, URL, bot_user_name
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

# Set Database
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, nullable=False)
    msg = db.Column(db.String(280), nullable=True)
    bot = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<Message {}>'.format(self.chat_id)

    def save_message(chat_id, msg, bot):
        msg =  Message(chat_id=chat_id, msg=msg, bot=bot)
        db.session.add(msg)
        db.session.commit()

db.create_all()

@app.route('/{}'.format(bot_token), methods=['POST'])
def request_telegram():
    # Get Telegram object and attributes
    print(request.__dict__)
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    msg_id = int(update.message.message_id)
    chat_id = int(update.message.chat.id)
    text = update.message.text.encode('utf-8').decode()

    # Save User Message
    Message.save_message(chat_id, text, False)

    # The first message to send for user
    if text == "/start":
        start_msg = """
        Bem-vindo ao FizzBuzz!
        Para começar digite um número inteiro múltiplo de 3 e/ou 5, com até 280 dígitos.
        Para ver todas as mensagens digite /messages
        """
        bot.sendMessage(chat_id=chat_id, text=start_msg, reply_to_message_id=msg_id)
    
    # Command to view all messages this chat
    elif text == "/messages":
        msgs = Message.query.filter_by(chat_id=chat_id)
        all_msg = ""
        for msg in msgs:

            if msg.bot:
                msg_temp = "{}: {} \n".format(bot_user_name, msg.msg)
            else:
                msg_temp = "You: {} \n".format(msg.msg)

            all_msg += msg_temp
            
        bot.sendMessage(chat_id=chat_id, text=all_msg, reply_to_message_id=msg_id)

    else:
        try:
            # FizzBuzz Logic
            if text.isdigit() and len(text) < 281:
                num = int(text)

                if num % 3 == 0 and num % 5 == 0:
                    msg_response = "FizzBuzz"
                elif num % 3 == 0:
                    msg_response = "Fizz"
                elif num % 5 ==0:
                    msg_response = "Buzz"
                else:
                    msg_response = "Digite um número inteiro múltiplo de 3 e/ou 5, com até 280 dígitos."
        
                Message.save_message(chat_id, msg_response, True)
                bot.sendMessage(chat_id=chat_id, text=msg_response, reply_to_message_id=msg_id)

            else:
                msg_response = "Digite um número inteiro múltiplo de 3 e/ou 5, com até 280 dígitos."
                Message.save_message(chat_id, msg_response, True)
                bot.sendMessage(chat_id=chat_id, text=msg_response, reply_to_message_id=msg_id)


        except Exception:
            msg_response = "O FizzBuzz volta em breve!"
            Message.save_message(chat_id, msg_response, True)
            bot.sendMessage(chat_id=chat_id, text=msg_response, reply_to_message_id=msg_id)

    return 'ok'

@app.route('/')
def index():
    hook = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    text = """
    <h3>Telegram Bot  - Teste para Desenvolvedores Python (cloudia).</h3>
    <p>Github: <a href="https://github.com/amandacpsantos/acps_bot"> Teste para Desenvolvedores Python (cloudia).</a></p>
    <p>Telegram Bot: <a href="https://t.me/acps_bot">@acps_bot</a></p>
    """
    return text

if __name__ == '__main__':
    app.run(threaded=True, debug=False)