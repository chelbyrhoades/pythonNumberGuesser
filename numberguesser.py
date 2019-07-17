import random

print("Welcome to Number Guesser. Choose your bounds!")

min = int(input("What's the lowest value possible?"))
max = int(input("What's the highest value possible?"))

number = random.randint(min, max)
count = 0
while True:
	guess = int(input("Guess a number: "))
	if guess == number:
		print("YAY you won!")
		break
	elif guess > number:
		print("Too high!")
		count += 1
	elif guess < number:
		print("Too low")
		count += 1
	elif count == 10:
		print("You lost. Cmon man. The number was: ")
		print(number)
		break
	else:
		print("You broke the system.")