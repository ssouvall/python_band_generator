import random

print("Welcome to the Band Name Generator")
town_name = input("What is the name of the town you grew up in?")
print(f"{town_name} is a great place!")
pet_name = input("Now what is the name of your favorite pet?")
print(f"Wow {pet_name} sounds like a great pet name")
lucky = input("Ok, are you feeling lucky?")

if lucky.lower() == 'yes':
    randomNum = random.random()
    print(f"Your lucky number is {randomNum * 10}. Congratulations!")
else:
    print(f"Your band name should be {town_name} {pet_name}!")
