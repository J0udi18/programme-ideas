import random


def display_tittle():
    tittle = "Simple Math Quiz"
    print("*" * len(tittle))
    print(tittle)
    print("*" * len(tittle))


def display_options():
    list_options = ["1.Addition", "2.subtraction", "3.multiplication", "4.Division", "5.Exit"]
    for option in list_options:
        print(option)
        print("-" * 20)


# Get user option
def get_userinput():
    operation = int(input("Enter operation of your choice: "))
    while operation > 5 or operation < 1:
        print("invalid menu option.try again..")
        operation = int(input("Enter operation of your choice: "))
        return operation


def get_usersolution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input("="))
    return result


def get_porblem(operation):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if operation==1:
        print("nu")


def main():
    display_tittle()
    display_options()
    option = get_userinput()
    print(option)
    prob = "2+6"
    user_answer = get_userinput(prob)
    print("user answer")


main()
