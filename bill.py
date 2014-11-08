def tip():
	subtotal = raw_input("What is the total before tax and tip? ")
	subtotal = int(subtotal) # convert string to integer
	mytax = 0.09 # meals tax in Florida is 9%, in many cities 
	mytip = 0.2 # assuming a 20% tip
	print "Please provide your bill ammount." 
	bill = raw_input("> ") 
	print ( “Your bill with tip and tax is: “)
	print( bill + ( ( bill + ( bill*mytax ) )  * mytip ) )
