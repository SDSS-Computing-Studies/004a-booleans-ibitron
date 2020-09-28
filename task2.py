#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"
a = input("Number")
a = int(a)
if a == 0:
 print("Number is 0") 
if a > 0:
 print("Number is Positive")
if a < 0:
 print("Number is Negative")
