height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_integer = float(height)
weight_integer = int(weight)


bmi = weight_integer / height_integer ** 2

bmi_as_integer = int(bmi)

print(bmi_as_integer)

