#! python3

# Have the user enter in a sentence. 
# Check to see if the word "password" is located in the sentence

# Inputs:
# a sentence

# Outputs:
# "the sentence contains password"
# "the sentence does not contain password"
a = input("Enter Password")

if "password" in a:
     print("The sentence contains password")
else:
    print("The sentence does not contain password")
