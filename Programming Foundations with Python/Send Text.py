from twilio.rest.client import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC5b51bfbf36c850f5c10b9b86af4fa4dc"
auth_token  = "{{ be3c46dc3e484a1820c3ebf880645a2c }}"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+16177772151",    # Replace with your phone number
    from_="+6179257836") # Replace with your Twilio number
print message.sid
