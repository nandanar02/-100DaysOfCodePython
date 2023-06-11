#assignment_1
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
a=two_digit_number[0]
b=two_digit_number[1]
c=str(int(a)+int(b))
# print(a +" "+ "+"+" " + b + " "+ "=" +" "+ c)
print(c)
---------------------------------------------------------------------
#assignment_2
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height1=float(height)
weight1=int(weight)
bmi=weight1/height1**2
print(int(bmi))
---------------------------------------------------------------------
# assignment_3
print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
percentage_of_tip=int(input("What percentage of tip would you like to give? 10, 12 or 15?\n"))
num_of_people=int(input("How many people to split the bill?\n"))
final_bill=round((bill+bill*percentage_of_tip/100)/num_of_people,2)
print(f"Each person should pay: ${final_bill}")
