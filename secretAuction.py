import os


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''



bidLog={}
flag= False
def getBid():
    name=input("Enter your name : ")
    bid=int(input("Enter your bid : $"))
    bidLog[name]=bid
def getWinner(dict):
    bid=0
    name=""
    for key in dict:
        if dict[key]>bid:
            name=key
            bid=dict[key]
    winner={}
    winner[name]=bid
    return winner



while not flag:
    print(logo)
    getBid()
    choice=input("Are there any other bidders? Y: yes, N: no -> ").lower()
    if choice=="n":
        flag= True
    os.system('cls')


winner=getWinner(bidLog)
for key in winner:
 print(f"The winner is {key} with a bid of ${winner[key]}.")
 input()




