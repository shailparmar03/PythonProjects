import random

n_letters=int(input("Enter the number of alphabets you want :"))
n_symbols=int(input("Enter the number of symbols you want   :"))
n_number= int(input("Enter the number of numbers you want   :"))

password=[]
for i in range(0,n_letters):
    password.append(chr(random.choice([random.choice(range(65, 91)),random.choice(range(97, 123))])))
print(password)

for i in range(0,n_symbols):
    password.append(random.choice(["!","@","$","#","%","^","&","*","(",")"]))
print(password)

for i in range(0,n_number):
    password.append(str(random.choice(range(0,10))))
print(password)

pssStr=""
print(pssStr.join(password))
print(password)
random.shuffle(password)
print(password)