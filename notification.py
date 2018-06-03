class Notification():
    hotels = []
    coustomer_list = []
    reservation_list = []

def __init__(self, customer_number, phone_number):
    self.customer_number = customer_number
    self.phone_number = str(phone_number)
    
from twilio.rest import Client


account_sid = "AC01de594b836ba445d77cbcba5b0074fc"

auth_token  = "fb9fd973a00a6f406b6860db56cc433c"

client = Client(account_sid, auth_token)

message = client.messages.create(to="+966554430150",from_="+13522928117",body="confirmation")

print(message.sid)
