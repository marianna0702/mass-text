# Marianna Moawad - 5/13/20
# Instructions and Inspiration: https://pypi.org/project/py-iMessage/

from py_imessage import imessage
import csv

contactList = {}

# opening txt file of message
f = open("message.txt", "r")
message = f.read()
print("Message is -> " + message)

# opening csv file with contacts
with open('contacts.csv', mode='r') as csv_file:
     csv_reader = csv.reader(csv_file)
     # ignore first line
     next(csv_reader)
     for row in csv_reader:
        contactList[row[0]] = row[1]

# messaging each person 
for person in contactList.keys():
    print("Sending a message to " + person)
    # message = "Hey " + person + " How are you?"
    phone = contactList[person]
    guid = imessage.send(phone, message)


