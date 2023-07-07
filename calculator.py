def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
n1=int(input("Enter the first number : "))
print("Choose an operation form the following :")
for symbol in operations:
    print(symbol)
user_choice=input()
n2=int(input("Enter the second number : "))
operation=operations[user_choice]
print(operation(n1,n2))
