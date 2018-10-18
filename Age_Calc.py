#age_calculator
name = input("Please enter your name: ")

while True:
	birth_year = input("What year were you born? ")
	try:
		birth_year = int(birth_year)
	except:
		ValueError
		print("Please enter a number")
		continue
	else:
		break

current_year = 2019

age = current_year - birth_year
turn_25 = (25-age) + current_year
turn_50 = (50 - age) + current_year
turn_75 = (75 - age) + current_year
turn_100 = (100 - age) + current_year

if turn_25 > current_year:
	print(f"Hey! {name} will turn 25 in {turn_25}")
if turn_50 > current_year:
	print(f"Hey! {name} will turn 50 in {turn_50}")
if turn_75 > current_year:
	print(f"Hey! {name} will turn 75 in {turn_75}")
if turn_100 > current_year:
	print(f"Hey! {name} will turn 100 in {turn_100}")
if age > 100:
	print(f"Wow! {name} you are {age}!!! Are you actually Nicholas Flamel?")
