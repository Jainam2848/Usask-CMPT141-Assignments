# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141

n_games = int(input("Number of games played :"))
time_per_game = int(input("What was average lenght of the game ? :"))
n_players = int((input("Number of players escorted ? :")))
price_per_player = float(input("How much did each player paid (in dollars)?:"))
tips = float(input("How much money was received in tips (in dollars) ? :"))


def time(n_games, time_per_game):
    """ Time function will use number of games and time per game(in minutes) as parameters
        and will calculate  total time spent for the games in hours"""

    total_time = n_games * time_per_game / 60
    return total_time


def revenue(tips, n_players, price_per_player):
    """ revenue function will take amount earned from tips ,
            number of players escorted and price to escort per player as parameters
            and will calculate total revenue generated"""

    total_revenue = tips + (n_players * price_per_player)
    return total_revenue


def rate_of_pay(revenue, time):
    """
    rate_of_pay  function will take function :time and revenue, as parameters 
    because functions are objects and can be taken as parameters in other function.
    We will calculate the pay rate by formula revenue/time
    a variable is assigned the value of revenue generated
    b variable is assigned the value of total time spent in hours.
    """
    a = revenue(tips, n_players, price_per_player)
    b = time(n_games, time_per_game)
    pay_rate = a / b
    return pay_rate


print("Revenue :", revenue(tips, n_players, price_per_player), "$")
print("Time :", time(n_games, time_per_game), "hours")
print("Pay rate :", rate_of_pay(revenue, time), "$/hour")
