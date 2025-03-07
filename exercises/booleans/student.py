def can_vote(age):
    return age >= 18

def free_ticket(age):
  return age < 12 or age >= 65

def close_enough(x, y):
   return y + 0.1 >= x >= y - 0.1

def is_divisible(a, b):
   return (a % b) == 0

def is_valid_month(month):
   return 1 <= month <= 12

def is_leap_year(year):
   return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def has_30_days(month):
   return month == 4 or month == 6 or month == 9 or month == 11

def has_31_days(month):
   return month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12

def has_28_days(month, year):
   return month == 2 and not is_leap_year(year)

def has_29_days(month, year):
   return month == 2 and is_leap_year(year)

def is_valid_date(day, month, year):
   return is_valid_month(month) and (
      (has_31_days(month) and (1 <= day <= 31)) or (has_30_days(month) and (1 <= day <= 30)) or ((has_28_days(month, year)) and (1 <= day <= 28)) or (has_29_days(month, year) and (1 <= day <= 29)))
   
def earlier(h1, m1, h2, m2):
   return (h1 < h2) or (h1 == h2 and m1 < m2)

def higher_card(card1, card2):
   return (card2 != 1) and (card1 > card2 or card1 == 1)
