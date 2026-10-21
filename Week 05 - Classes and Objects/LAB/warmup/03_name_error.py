# Run it, read the last line, then fix it.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        return "OVER LIMIT" if self.value > self.limit else "OK"

r = Record("R-001", 120.0, 100.0)
print(r.status())


# the error here is that "status" is not defined properly. We have to add "r." to status. We want to call the method.
