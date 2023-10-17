from math import floor, ceil

def five():
    return 5

def triple (x):
    return x * 3

def average (x, y):
    return (x + y) / 2

def distance(x1, y1, x2, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)

def buses_needed(people_count, bus_capacity):
    return ceil(people_count / bus_capacity)

def pizza(n_people, slices_per_pizza):
    return ceil(n_people / slices_per_pizza)

def cake(eggs):
    return (eggs // 5)

def candy_per_child(candy_count, child_count):
    return (candy_count // child_count)

def cake2(eggs, flour):
    a = eggs // 5 
    b = flour // 250
    return min(a, b)

def cake3(eggs, flour, butter, sugar):
    a = eggs // 5 
    b = flour // 250
    c = butter // 200
    d = sugar // 250
    return min(a, b, c, d)

def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    a = eggs // eggs_per_cake
    b = flour // flour_per_cake
    c = butter // butter_per_cake
    d = sugar // sugar_per_cake
    return min(a, b, c, d)

def hours(duration):
    return (duration // 3600)

def minutes(duration):
    h = hours(duration)
    return (duration - (h * 3600)) // 60

def seconds(duration):
    h = hours(duration)
    m = minutes(duration)
    return (duration - (h * 3600) - (m * 60))

def coins(amount):
    five_coins = amount // 5
    total_value_five_coins = five_coins * 5
    two_coins = (amount - total_value_five_coins) // 2
    total_value_two_coins = two_coins * 2
    coins = amount - total_value_five_coins - total_value_two_coins
    return five_coins + two_coins + coins

def leftover_candy(candy_count, child_count):
    return candy_count % child_count

def internet_costs(duration_in_seconds, cost_per_block):
    block = ceil(duration_in_seconds / 360)
    return block * cost_per_block

def middle(a, b, c):
    laagste = min(a, b, c)
    hoogste = max(a, b, c)
    return (a + b + c) - laagste - hoogste 

def last_digit(n):
    return (n % 10)

def drop_last_digit(n):
    return (n // 10)

def next_player(player, player_count):
    return (player + 1) % player_count

def next_player2(player, player_count):
    return (player % player_count) + 1




