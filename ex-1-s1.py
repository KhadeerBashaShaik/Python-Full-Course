class TicketBooker:
    def Ticket(self):
        print("Good Morning Sir,How Can I help you...?\n")


class Person(TicketBooker):
    def Falcon(self):
        print("Good Morning, My Name is Falcon\n")
        print("Can you help me by booking the Ticket for Upcoming Train\n")


class Booking(TicketBooker):
    def Booking(self):
        A=int(input("Sure Sir,\n\n\tEnter Number of seats for booking="))
        B=input("\n\tEnter the Destination Station Name=\t")
        C=input("\n\tEnter Mobile Number=\t")
        D=250
        print("\nSeats=",A)
        print("Destination Place=",B)
        print("Phone Number=",C)
        print(f"the amount to be payed: {A * D}")


class ConfirmBooking(Booking,TicketBooker):
    def Confirm(self):
        print(" The Tickets will be messaged to Your Number Phone Number")
        print("\n\t\tYour Tickets are Confirmed")

a=Booking()
a.Ticket()
b=Person()
b.Falcon()
a.Booking()
c=ConfirmBooking()
c.Confirm()