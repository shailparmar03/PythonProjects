import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

life= len(HANGMANPICS)
movies=["spiderman","ironman","batman","antman"]

choice=random.choice(movies)
length=len(choice)

display=[]
for _ in range(length):
    display+="_"

gameComplete=False
print("The movies choosen is : ",choice)
while life>0 and gameComplete == False :
    print(HANGMANPICS[7-life])
    print(display)

    userInput=input("Enter a letter : ").lower()

    if userInput in choice:
        for pos in range(length):
            if choice[pos]==userInput:
                display[pos]=userInput
    else:
        life-=1

    if "_" not in display:
        gameComplete=True
        print("You won")
    if life == 0:
        print("You loose")



