
# Function definition
def caught_speeding(speed, is_birthday):
    speed_limit = 60
    
    if is_birthday == True:
        speed_limit += 5

    if speed <= speed_limit:
        return "No ticket"
    elif speed_limit + 1 < speed <= speed_limit + 20:
        return "Small Ticket"
    elif speed_limit + 21 <= speed:
        return "Big Ticket"
