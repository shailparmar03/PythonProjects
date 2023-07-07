import random
import art
import gameData
import os

correct_guess = True
score = 0


def update_score():
    global score
    score += 1


def check_guess(user_guess, other_option):
    if user_guess['follower_count'] > other_option['follower_count']:
        update_score()
        os.system('cls')
    else:
        global correct_guess
        correct_guess = False
        os.system('cls')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")


opponents = random.sample(gameData.data, k=2)
while correct_guess:
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score:{score}")
    A = opponents[0]
    print(f"COMPARE A: {A['name']}, {A['description']}, {A['country']}")
    print(art.vs)
    B = opponents[1]
    print(f"AGAINST B:  {B['name']}, {B['description']}, {B['country']}")
    player_guess = input("Who has more followers? Type 'A' or 'B':").upper()
    if player_guess == 'A':
        check_guess(A, B)
    elif player_guess == 'B':
        check_guess(B, A)
input()
