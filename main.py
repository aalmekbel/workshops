from hotel import Hotel
from customer import Customer
from reservation import Reservation
# from notification import Notification


def start_app():
	rotana_hotel = Hotel(20,"Rotana","Abu Dhabi",200,40)
	sheraton_hotel = Hotel(21,"Sheraton","Abu Dhabi",300,100)
	print Hotel.hotels
	print rotana_hotel.list_hotels_in_city()
start_app()

def customer_list():
	customer_list = ("Ahmed", "0685555")
	print Customer.customers
customer_list()


