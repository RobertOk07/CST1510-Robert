# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"

print(check(87, 100))


# here the problem is that the function "status" does not exist. Here we have the function "check" given. So we just have to change the function
# to the value in print from "status" to "check" and we have to add the print function before the check function also.