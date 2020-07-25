from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse as msg.respond
import requests

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def WhatsApp_Bot():
    incoming_msg = request.values.get('Body', '').lower()
    outgoing_message = msg.respond()
    msg = outgoing_message.message()
    responded = False
    if 'quote' in incoming_msg:
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(outgoing_message)
