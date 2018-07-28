TICKET_PRICE = 10
tickets_remaining = 100

while tickets_remaining >= 1:
	print("There are {} tickets remaining.".format(tickets_remaining))

	name = raw_input("Welcome. What is your name? ")

	quantity = raw_input("Hello, {}. How many tickets would you like to purchase?  ".format(name))
	try:
		quantity = int(quantity)
		#Raise ValueError if the request is for more tickets than available
		if quantity > tickets_remaining:
			raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
	except ValueError as err:
		print("We ran into an issue. {} Please try again.".format(err))
	else:
		amount_due = quantity * TICKET_PRICE
		print("The total due is ${}".format(amount_due))

		proceed = raw_input("To contunue with your order? Y/N  ")

		if (proceed.lower() == "y"):
			#TODO: Gather credit card info and process
			print("SOLD!")
		
			tickets_remaining -= quantity
		else:
			print("Thank you anyways, {}!".format(name))
	
print("Sorry the tickets are all sold out :(")

