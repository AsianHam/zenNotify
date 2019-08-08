from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket
from win10toast import ToastNotifier

creds = {
    'email' : 'spstech@columbia.edu',
    'password' : '%$MjiKirk106%*',
    'subdomain' : 'spsservice'
}

zenpyClient = Zenpy(**creds)
toaster = ToastNotifier()

newTicket = []

for ticket in zenpyClient.search(type='ticket', status='new'):
    if ticket not in newTicket:
        newTicket.append(ticket)
        text = "Check ticket: " + str(ticket)
        toaster.show_toast("New Ticket", text, duration = 15)
    else:
        continue