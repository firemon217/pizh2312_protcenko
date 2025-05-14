from ticketArrive import *
from unlimitedTicket import *
from restrictionsTicket import *
from restrictionsTravelTicket import *

ticket = RestrictionsTravelTicket("Goose", 500, 30)
ticket.off_a_trip()
print(ticket)