#Madlibs game
def madlibs():

    adj1 = input("Enter a adjective (description): ")
    noun1 = input("Enter a noun (person, place, thing): ")
    adj2 = input("Enter a adjective (description): ")
    verb1 = input("Enter a verb ending with 'ing': ")
    adj3 = input("Enter a adjective (description): ")

    print(f"I went to a {adj1} zoo today.")
    print(f"In an exhibit I saw a {noun1}!")
    print(f"{noun1} was {adj2} and {verb1}")
    print(f"I was {adj3}")


# Simple Arithmetic Calculator	
def calculator():
    print("Welcome to a simple Arithmetic Calculator!!!")

    while True:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        op = int(input("Please choose the number corresponding to the operation!!\n 1. Addition(+) \n 2. Subtraction(-) \n 3. Multiplication(x) \n 4. Division(÷) \nChoose: "))

        if op == 1:
            ans = num1 + num2
            print(round(ans, 3))
        elif op == 2:
            ans = num1 - num2
            print(round(ans, 3))
        elif op == 3:
            ans = num1 * num2
            print(round(ans, 3))
        elif op == 4:
            if num2 != 0:
                ans = num1 / num2
                print(round(ans, 3))
            else:
                print("Can't divide by 0!")
        else:
            print("Invalid Operator!")

        ch = input("Do you want to calculate again(y/n): ").lower()
        if ch == "y":
            continue
        else:
            break


# Weight Converter
def weight():
    print("Weight converter")

    weight = float(input("\nEnter your Weight: "))
    unit = input("Killograms(K) or Pounds(L): ").lower()

    if unit == "k":
        res = weight * 2.205
        unit = "lbs"
        print(f"\nYou weigh {round(res, 2)} {unit}.")
    elif unit == "l":
        res = weight / 2.205
        unit = "kg"
        print(f"\nYou weigh {round(res, 2)} {unit}.")
    else:
        print(f"{unit} is not a valid unit!!")


#Temperature Converter
def temp():
    temp = float(input("Enter teperature: "))
    unit = input("Celcius(C) or Fahrenheit(F): ").lower()

    if unit == "c":
        res = round(temp *(9/5) + 32, 1)
        print(f"Temperature is around {res}° F.")
    elif unit == "f":
        res = round((temp - 32) * 5/9, 1)
        print(round(res, 2))
        print(f"Temperature is around {res}° C.")
    else:
        print("Unit of measurement must be either Celcius(C) or Fahrenheit(F)!")
    

#Email Slicer
def email():
    email = input("Enter your email: ")

    index = email.index("@")

    username = email[:index]
    domain = email[index + 1 :]

    print(f"Your username is {username} and your domain is {domain}")


#Compound Interest Calculator
def interest():
    p = float(input("Enter the initial principal balance $: "))
    r = float(input("Enter the interest rate %: "))
    t = int(input("Enter the amount of time: "))

    res = round(p * (1 + ((r / 100))) ** t, 2)
    print(f"You will have ${res} in {round(t, 0)} years.")


#Countdown Timer
def timer():
    import time

    my_time = int(input("Enter the time in seconds: "))

    for i in range(my_time, 0, -1):

        s = i % 60
        m = int((i / 60) % 60)
        h = int(i / 3600)

        print(f"{h:02}:{m:02}:{s:02}")        
        time.sleep(1)
    
    print("TIME'S UP!!!")


#Shopping Cart Program
def cart():
    foods = []
    prices =[]
    total = 0

    while True:
        food = input("Enter a food to buy (q to quit): ")
        if food.lower() == "q":
            break
        else:
            price = float(input(f"Enter the price of {food}: $"))
            prices.append(price)
            foods.append(food)
    
    print("<-----YOUR CART ------>\n")

    for food in foods:
        print(food, end="  ")
    
    for price in prices:
        total += price
    
    print(f"\n\nYour total is: ${total}")


#Quiz Game
def quiz():
    ques = ()
    opt = ()


#Suitable for PLayground or Not
def print_playground_message():
    try:
        age = int(input("Enter your age: "))
        if age < 0 :
            print("Sorry, your age is invalid!")
            return
        if age < 16:
            print("Welcome!")
        else:
            print("Sorry, you're too old!")
    except ValueError:
        print("Sorry, your age is invalid!")


#RUN
if __name__ =="__main__":
     print_playground_message()
