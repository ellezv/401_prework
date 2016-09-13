def hotel_cost(nights) :
    return 140*nights

def plane_ride_cost(city) :
    if city == "Charlotte" :
        return 183
    elif city == "Tampa" :
        return 220
    elif city == "Pittsburgh" :
        return 222
    elif city == "Los Angeles" :
        return 475

def rental_car_cost(days) :
    if days >= 7 :
        cost = (days*40)-50
        return cost
    elif days >= 3 :
        cost = (days*40)-20
        return cost
    else :
        cost = days*40
        return cost

def trip_cost(city, days, spending_money) :
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)