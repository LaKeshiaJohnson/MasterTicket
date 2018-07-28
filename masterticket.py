#Run code until tickets run out
#Output how many tickets remaining using tickets_remaining variable
#Gather the user's name and assign it to a new variable
#Prompt user by name to ask how many tickets they would like
#Calculate price and output to screen
#Prompt user if they want to continue. Y/N
#if they want to proceed print out to the "SOLD!" to confirm purchase and updated number of tickets remaining
#otherwise, thank them by name
#Notify users when tickets are sold out

TICKET_PRICE = 10
tickets_remaining = 100

def calculate_price(quantity):
	return quantity * TICKET_PRICE


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
		amount_due = calculate_price(quantity)
		print("The total due is ${}".format(amount_due))

		proceed = raw_input("To contunue with your order? Y/N  ")

		if (proceed.lower() == "y"):
			#TODO: Gather credit card info and process
			print("SOLD!")
		
			tickets_remaining -= quantity
		else:
			print("Thank you anyways, {}!".format(name))
	
print("Sorry the tickets are all sold out :(")

