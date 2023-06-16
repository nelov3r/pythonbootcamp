print("Welcome to the rollercoaster!")
height = int(input ("What is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("pay 5 dollars for a ticket")
    elif age <= 18:
        print("PLease pay 7 dollars for a ticket")
    elif age == 90:
        print("u fucking old man :()")
    else:
        print("Please py 100 dollars for a ticket!")
else:
    print("Sorry u have to be taller :)))")
    