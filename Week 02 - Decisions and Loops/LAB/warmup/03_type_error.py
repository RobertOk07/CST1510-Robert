# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = int(input("Value: "))

if value > limit:
    print("OVER")
else:
    print("OK")

#We know that the function "input" does not display a number regardless of what you do, so here we have to difine the input as either a int or float. 
#For this example i use int, due to the reason we have a Number without a decimal

