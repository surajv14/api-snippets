# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

trigger = client.usage.triggers("UT33c6aeeba34e48f38d6899ea5b765ad4").update(
    friendly_name="Monthly Maximum Call Usage",
    callback_url="https://www.example.com/monthly-usage-trigger"
)

print(trigger.date_fired)
