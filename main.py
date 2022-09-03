import random
import os, sys
from art import logo


def pick_random_card():
    """Returns a random card from the deck"""
    return random.choice(cards)


def c_score_dealer():
    """Returns current score from dealer_hand"""
    score_dealer = 0
    for score in dealer_hand:
        score_dealer += score
    return score_dealer


def c_score_user():
    """Returns current score from user_hand"""
    score_user = 0
    for score in user_hand:
        score_user += score
    return score_user


def blackjack():
    """Check if there is blackjack on the first cards"""
    ace = 11
    if c_score_user() == 21:
        if (ace in user_hand and
                10 in user_hand):
            return print("Blackjack, you win"), exit()
    if c_score_dealer() == 21:
        if (ace in dealer_hand and
                10 in dealer_hand):
            return print("You lose"), exit()
    if c_score_user() > 21:
        if ace in user_hand:
            user_hand[user_hand.index(11)] = 1
            c_score_user()
            if c_score_user() > 21:
                return print("You lose"), exit()
        else:
            return print("You lose"), exit()


cards = [
    11, 2, 3,
    4, 5, 6,
    7, 8, 9,
    10, 10, 10
]
# TEST
# user_hand = [10, 10]
endgame = True
while endgame:
    dealer_hand = [pick_random_card(), pick_random_card()]
    hide_dealer_card = [dealer_hand[0]]
    print(f"Dealer cards : {hide_dealer_card}")
    user_hand = [pick_random_card(), pick_random_card()]
    print(f"Your cards : {user_hand}, current score :{c_score_user()}")
    blackjack()

    while (c_score_user() or c_score_dealer()) <= 21:
        hit_or_stand = input("You want one more card?. Type 'hit' or 'stand': ").lower()
        if hit_or_stand == "hit":
            # TEST
            # user_hand += [11]
            user_hand += [pick_random_card()]
            blackjack()
            print(f"Your cards : {user_hand}, current score :{c_score_user()}")
            if c_score_user() == 21:
                print("Blackjack!, you win")
                break
            if c_score_user() > 21:
                print("You lose")
                break
        if hit_or_stand == 'stand':
            print(f"Dealer cards : {dealer_hand}, current score : {c_score_dealer()}")
            if c_score_user() == 21:
                print("You win")
                break
            while c_score_dealer() < 17:
                print("Dealer draw a card")
                dealer_hand += [pick_random_card()]
                print(f"Dealer cards : {dealer_hand}, current score : {c_score_dealer()}")
            if c_score_dealer() > c_score_user() and not c_score_dealer() > 21:
                print("Dealer win")
            elif c_score_dealer() == 21:
                print("Dealer win")
            elif c_score_dealer() > 21:
                print("You win")
            if c_score_dealer() < c_score_user():
                print("You win")
            if c_score_dealer() == c_score_user():
                print("It's a tie")
            break
    endgame = input("Do you want play a new game?. Type 'Yes' or 'No'").lower()
    if endgame == 'no':
        endgame = False
