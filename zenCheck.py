from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket
from win10toast import ToastNotifier
import time

creds = {
    'email' : 'spstech@columbia.edu',
    'password' : '%$MjiKirk106%*',
    'subdomain' : 'spsservice'
}

toaster = ToastNotifier()

newTicket = []

while 1 != 2:
    zenpyClient = Zenpy(**creds)
    for ticket in zenpyClient.search(type='ticket', status='new'):
        if str(ticket) in newTicket:
            continue
        else:
            newTicket.append(str(ticket))
            text = str(ticket.subject)
            toaster.show_toast("New Ticket", text, duration = 10)
    time.sleep(30)