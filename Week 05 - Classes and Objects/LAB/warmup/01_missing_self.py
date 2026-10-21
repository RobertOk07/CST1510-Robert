# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self,percent):    # this parameter should be self
        return percent

r = Record()
print(r.status(95))

# We had to add "self" next to percent.
