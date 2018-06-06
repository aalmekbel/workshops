class Hotel():
    hotels = []
    def __init__(self, number, hotel_name, city,total_rooms, empty_rooms):
        self.number = number
        self.hotel_name = hotel_name
        self.city = city
        self.total_rooms = total_rooms
        self.empty_rooms = empty_rooms

        Hotel.hotels.append([self.number , self.hotel_name, self.city, self.total_rooms, self.empty_rooms])

def list_hotels_in_city(self, city):
    # search inside Hotel.hotels for hotels in a "city"
    self.city = city
    for hotel in range(len(Hotel.hotels)):
        if Hotel.hotels["city"]==self.city:
            print self.city


