"""
Twilio 
datetime  module 
time 
1- twilion client setup 
2 - user input 
3 - scheduling logic 
4 - send messages

"""-
#step 1 install required libraries 

from twilio.rest import Client
from datetime import datetime , timedelta
import time 

#step 2 twilio credentials 
account_sid = "put your token here "
auth_token = "put your token here "

client = Client(account_sid , auth_token)

#step 3 design send message function

def send_whatsapp_message(recipient_number , message_body):
    try:
        message = client.messages.create(
           from_= "whatsapp:+14155238886",
           body = message_body,
           to = f"whatsapp:{recipient_number}"
           )
        print(f"Message sent succesfully! Message SID{message.sid}")
    except Exception as e:
        print("AN ERROR OCCURRED")

# step 4 useer input 
name = input("enter the recipient name = ")
recipient_number = input("enter the recipient number with countrty code ( e.g: +12345): ")
message_body = input(f"enter the message you want to send{name}: ")

#step 5 parse date/time and calculate delay 
date_str = input("enter the date to send the message (YYYY-MM-DD): ")
time_str = input("enter the time to send the message (HH:MM in 24 hours formate ): ")    

#datetime 
schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay 
time_difference = schedule_datetime-current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The specified time is in the past Please enter a future date and time: ")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}.")

    #wait untill the scheduled time 
    time.sleep(delay_seconds) #1000

    #send the messsage 
    send_whatsapp_message(recipient_number, message_body)
