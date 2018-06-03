class Reservation():
    reservations = []
def __init__(self, number,hotel_name, city,total_rooms,empty_rooms):
    self.number = number
    self.hotel_name = hotel_name
    self.city = city
    self.total_rooms = total_rooms
    self.empty_rooms = empty_rooms

def reserve_room (hotel_name, customer_name):
    for empty_rooms in hotel_name:
        empty_rooms>=1
        return True
        print "confirmation"
    else:
        return Fales
        print "sorry no rooms available"
 

def add_new_reservation(hotel_name, customer_name):
    if reserve_room(hotel_name, customer_name):
        return True
    add_new_reservation.append([hotel_name, customer_name])

