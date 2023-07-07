############### Blackjack Project #####################
import random
import os

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def initialize():
    user = []
    dealer = []
    user.extend(random.choices(cards,k=2))
    dealer.extend(random.choices(cards,k=2))
    return user,dealer

continue_game=True

def printCurrentStatus(current_user,current_dealer):
    print(f"User cards :{current_user}, current score:{sum(current_user)}")
    print(f"Computer's first card is {current_dealer[0]}")

def aceCheck(cards):
    if 11 in cards and sum(cards) > 21:
        index_11=cards.index(11)
        cards[index_11]=1

def finalScore(user,dealer):
    print(f"Your final hand {user},final score: {sum(user)}")
    print(f"Computer's final hand {dealer},final score:{sum(dealer)}")

def gameplay():
    continue_picking = input("Press 'y' to pick and 'n' to pass :").lower()
    if continue_picking == 'y':
        user.append(random.choice(cards))
        aceCheck(user)
        printCurrentStatus(user,dealer)
        winnerCheck(sum(user),sum(dealer),"y")


    else:
        while sum(dealer)<16:
            dealer.append(random.choice(cards))
            aceCheck(dealer)
        print(dealer)
        winnerCheck(sum(user), sum(dealer),"n")



def winnerCheck(user_total, dealer_total,char=""):
    if user_total==dealer_total==21:
        finalScore(user,dealer)
        print("->Computer wins")

    elif user_total==21 :
        finalScore(user,dealer)
        print("->User wins")

    elif dealer_total==21:
        finalScore(user,dealer)
        print("->Computer wins")

    elif user_total>21:
        finalScore(user,dealer)
        print("->You went over. You loose!")

    elif dealer_total>21:
        finalScore(user,dealer)
        print("->Computer went over. You win!")
    elif user_total==dealer_total and char=="n":
        finalScore(user,dealer)
        print("->It's a draw!")
    elif user_total>dealer_total and char=="n":
        finalScore(user,dealer)
        print("->User wins")
    elif user_total<dealer_total and char== "n":
        finalScore(user,dealer)
        print("->Computer wins")
    else:
        gameplay()

while continue_game:
    playGameCheck=input("\nPress 'y' to play Game or 'q' to exit :").lower()
    if playGameCheck=="y":
        os.system('cls')
        print(logo)
        user,dealer=initialize()
        printCurrentStatus(user,dealer)
        winnerCheck(sum(user),sum(dealer))


    else:
        continue_game=False

















