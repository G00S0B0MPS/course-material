def total_cost(amount):
    if amount < 100:
        return amount + 10
    if amount >= 200:
        return amount * 0.95
    return amount

def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 
    
def rock_paper_scissors(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 0
    elif player1_choice == 0 and player2_choice == 2:
        return 1
    elif player1_choice == 2 and player2_choice == 0:
        return 2
    elif player1_choice > player2_choice:
        return 1
    else: 
        return 2
    
def player_movement(position, left_arrow, right_arrow, shift):
    if left_arrow:
        return position - 1
    if right_arrow:
        return position + 1
    if shift:
        return (left_arrow or right_arrow)*2
    return position