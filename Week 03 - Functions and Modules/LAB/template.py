"""
RECORD CHECK  -  my version
===========================

Name  :  Robert Dawid Okonski
Lane  :  IT
Date  : 11/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def status_of(percent, warning_at=90):
    """ it returns a status based on percentage givin"""
    if percent >= 100:
        return("OVER LIMIT")
    elif percent >= warning_at:
        return("WARNING")
    else:
        return("OK")

def check(value,limit):
    """returns difference and percentage as two different values"""
    difference= value-limit
    percent= (value/limit)*100
    return difference, percent

def print_report(label, value,limit, difference, percent, status):
    """ i am printing the cyber security report"""
    print(label, value,limit,difference, percent, status)
# ==================================================================== INPUT
while True:
    label = input("What is your hostname, Sir?")
    if label == "quit":
     break

    value = float(input(" How much GB did you use,Sir?"))
    limit =float(input("How much total GB do you have, Sir?"))

    # ================================================================== PROCESS
    difference , percent= check(value, limit)
    status = status_of(percent)
    #here we store the answer in status and i made use of D12, to know how to call a function and receive 2 values.
    # i am stuck with the excellent part.

    # =================================================================== OUTPUT
    print("=" * 30)
    print("RECORD CHECK  : ",label)
    print("=" * 30)
    print(f"Used GB  : {value:>10.2f}")
    print(f"Total GB : {limit:>10.2f}")
    print(f"Free GB  : {difference:>10.2f}")
    print(f"Percent  : {percent:>10.2f} %")
    print(f"Status   : {status:>10}")

# when using "0" as value the error i get is "ZeroDivisionError: division by zero"
# ==========================================================================

