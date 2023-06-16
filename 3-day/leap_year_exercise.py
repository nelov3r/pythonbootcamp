



def check_if_leap(year_var: int):
    divby4 = year_var % 4 == 0
    divby100 = year_var % 100 == 0
    divby400= year_var % 400 == 0
    
    print(f"Year {year_var}")
    if divby4:
        if divby100:
            if divby400:
                print("ITS A LEAP")
            else:
                print("NOT A LEAP")
        else:
            print ("ITS A LEAP")
    else:
        print("not leap")

check_if_leap(int(input("Enter year!")))