cmd in 

Then we need to activate the virtuell env:

python -m venv WhatsApp_Bot-venv
WhatsApp_Bot-venv\Scripts\activate
cd WhatsApp_Bot-venv
flask run

Copy port (Running on http://127.0.0.1:5000/) -> 5000

After that we run ngrok from our desktop:

ngrok http 5000

Copy url and add /WhatsApp_Bot (like https://2c64abe4.ngrok.io/WhatsApp_Bot) into:

https://www.twilio.com/console/sms/whatsapp/sandbox

under "WHEN A MESSAGE COMES IN".

done.