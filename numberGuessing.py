import random

logo=""""

  ____  __ __    ___  _____ _____     ______  __ __    ___      ____   __ __  ___ ___  ____     ___  ____  
 /    ||  |  |  /  _]/ ___// ___/    |      ||  |  |  /  _]    |    \ |  |  ||   |   ||    \   /  _]|    \ 
|   __||  |  | /  [_(   \_(   \_     |      ||  |  | /  [_     |  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )
|  |  ||  |  ||    _]\__  |\__  |    |_|  |_||  _  ||    _]    |  |  ||  |  ||  \_/  ||     ||    _]|    / 
|  |_ ||  :  ||   [_ /  \ |/  \ |      |  |  |  |  ||   [_     |  |  ||  :  ||   |   ||  O  ||   [_ |    \ 
|     ||     ||     |\    |\    |      |  |  |  |  ||     |    |  |  ||     ||   |   ||     ||     ||  .  |
|___,_| \__,_||_____| \___| \___|      |__|  |__|__||_____|    |__|__| \__,_||___|___||_____||_____||__|\_|

"""

print("Welcome to Guessing game!")
print("I am thinking of a number between 1 to 100.")

guessed_number=random.choice(range (1,100))
print(f"Pssst, the guessed number is {guessed_number}")

def chooseLevel():
    difficulty=input("Choose a difficulty level, 'e' for easy or 'h' for hard :").lower()
    if difficulty=="e":
        return 10
    else:
        return 5



print(logo)
attempts=chooseLevel()
while attempts!=0:
    print(f"You have {attempts} attempts remaining.")
    user_guess=int(input("Make a guess :"))
    if user_guess==guessed_number:
        print(f"You got it, the answer is {user_guess}")
        break
    elif user_guess>guessed_number:
        print("Too high, guess again")
        attempts-=1
    else:
        print("Too low, guess again")
        attempts-=1
if attempts==0:
    print("Attempts exhausted!")


