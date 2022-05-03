# This program says hello and asks for my name

print ("Hello World!")

print("What is your name?") # ask for their name
my_name = input()
print("It is good to meet your, " + my_name)
print("The length of your name is:")
print(len(my_name)) # count the chars in string

print("What is your age?")
my_age = input() # ask for the age
print("You will be " + str(int(my_age ) + 1) + " in a year")