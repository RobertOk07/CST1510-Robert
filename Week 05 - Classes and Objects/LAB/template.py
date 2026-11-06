"""
RECORD CHECK  -  my version
===========================

Name  : Robert Okonski
Lane  :  Cyber Security    
Date  : 25/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    over_limit_count = 0
    #Instructions say to add the over limit counter under my class-level.
    def __init__(self, label, value,limit):
        self.label= label
        self.value= value
        self.limit= limit

    def status(self):
        """ Calculares the percentage and gives back a record based on the limit and value"""
        percentage = (self.value/self.limit) * 100
        if percentage >= 100:
            Record.over_limit_count += 1 #I am counting the records that are over limit
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"
# ==================================================================== RECORDS
def load_records(path):
    """Reads the label,value,limit lines from a file and return a list of Records."""
    records = []
    # I created my own file in my LAB folder with my own values
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label,float(value), float(limit)))
    return records
records = load_records("records.txt")# Here i am loading my file so my function can make use of it. I am having problem with loading it, i keep getting back an error.
#  File "/Users/robertok/Desktop/Robert OK/ROBERT/School/Middelsex/Year 1/CST1510 Info/CST1510/Week 05 - Classes and Objects/LAB/template.py", line 39, in load_records
# This is the error """"with open(path) as f:
        #~~~~^^^^^^
#FileNotFoundError: [Errno 2] No such file or directory: 'records.txt'""""
# I don't understand why python is saying the file cant be found. It's in my LAB folder.
# ==================================================================== OUTPUT

for record in records:
    status= record.status()
    print("=" * 50)
    print("Record label:", record.label)
    print("Failed login attempts:", record.value)
    print("Total attempts:", record.limit)
    print("Status:", status)
    print("=" * 50)
    print("OVER THE LIMIT COUNT:", Record.over_limit_count)

# ==========================================================================

