# This program allows a user to plan their holiday and gives them the price
Destinations = ["London","Paris", "Rome"]
car_cost = {"London" : 40, "Paris" : 35, "Rome" : 30}
hotel_cost_per_city = {"London" : 90, "Paris" : 75, "Rome" : 65}

# Define the cost per night at the hotel.
def hotel_cost(num_nights, city_flight):
    cost_per_night = hotel_cost_per_city[city_flight]
    total_cost = num_nights * cost_per_night
    return total_cost

# Define the flight costs according to the city
def plane_cost(city_flight):
    if city_flight == "London":
        cost = 180
    elif city_flight == "Paris":
        cost = 210
    elif city_flight == "Rome":
        cost = 150
    else:
        cost = 110
    return cost

# Define the daily rental cost
def car_rental(rental_days,city_flight):
    cost_per_day = car_cost[city_flight]
    total_cost = rental_days * cost_per_day  # calculation for the dail rental cost
    return total_cost

# Definong holiday cost for the total of the whole holiday
def holiday_cost(num_nights, rental_days, city_flight):
    hotel_cost_val = hotel_cost(num_nights,city_flight)
    plane_cost_val = plane_cost(city_flight)
    car_rental_val = car_rental(rental_days,city_flight)
    total_cost = hotel_cost_val + plane_cost_val + car_rental_val
    return total_cost



city_flight = input("Enter the city you'll be flying to (options: London, Paris, Rome, other):\n> ").capitalize()
num_nights = int(input("Enter the number of nights you intend to stay:\n> "))
rental_days = int(input("Enter the number of days that you want to hire a car for:\n> "))

# Call the holiday_cost function to calculate the total cost of the holiday.
total_holiday_cost = holiday_cost(num_nights, rental_days, city_flight)

# Print out the details of the holiday in a readable way
print("Holiday plan:")
print("- You will be Flying to:", city_flight)
print("- You are Staying at a hotel for", num_nights, "nights")
print("- You are Hiring a car for", rental_days, "days")
print("- The total cost for the holiday will be:", total_holiday_cost)

    
    