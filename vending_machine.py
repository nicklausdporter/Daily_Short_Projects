sodas = ["Pepsi", "Cherry Coke", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snickers", "M&Ms", "Twizzlers"]

while True:
	choice = input("Would you like a SODA, some CHIPS, or a CANDY? ").lower()
	try:
		if choice == 'soda':
			snack = sodas.pop()
		elif choice == 'chips':
			snack = chips.pop()
		elif choice == 'candy':
			snack = candy.pop()
		else:
			print("Sorry, I didnt understand that.")
			continue
	except IndexError:
		print(f"We're all out of {choice}! Sorry!")
	else:
		print(f"Heres your {choice}: {snack}")
