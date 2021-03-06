# Download the Python helper library from twilio.com/docs/python/install
import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

number = client.api.account.incoming_phone_numbers.create(
    voice_url="http://demo.twilio.com/docs/voice.xml",
    phone_number="+15005550006"
)

print(number.sid)
