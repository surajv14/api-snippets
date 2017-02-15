# Download the **Next-Gen** twilio-python library from:
# twilio.com/docs/libraries/python#installation-nextgen
from twilio.rest import Client

# Your Account SID from www.twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"  # Your Auth Token from www.twilio.com/console

client = Client(account_sid, auth_token)

wireless = client.preview.wireless

plan = wireless.rate_plans('WP467fb57a0aba9641a8209136d42545f8').fetch()
print(plan.sid)
print(plan.alias)
