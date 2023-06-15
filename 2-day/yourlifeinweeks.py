age = int(input("What is your current age? "))

max_age = 90

ages_left = (max_age - age)
months_left = (ages_left * 12)
days_left = (ages_left * 365)
weeks_left = (days_left // 7)


print(f"You have {days_left}, {weeks_left} weeks, and {months_left} left.")
