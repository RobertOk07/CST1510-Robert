"""
RECORD CHECK  -  my version
===========================

Name  : Robert Okonski
Lane  : IT      
Date  : 18/10/2026

Run it:   python template.py
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

def check_record(value,limit): # it was "check" only before but i chenged it to "check_records". The instructions say so. And i added "Status"
    """returns difference, percentage and status"""
    difference= value-limit
    percent=(value/limit)*100
    status= status_of(percent)
    return difference, percent, status

def print_report(label, value,limit, difference, percent, status):
    """ All inputed calculations and values are printed"""
    print(label, value,limit,difference, percent, status)

def load_records(path):
    """Reads value, limit, label from a file and gives it back as a list of dicts."""
    records= []
    with open(path) as f:
        for line in f:
            label, value,limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })
    return records
load_records =("rob.txt") # I have a problem with loading my file, i dont know how to fix it.
# =============================================================== PROCESS + OUTPUT
for record in load_records:
    difference,percent, status = check_record(record["value"], record["limit"])
    
    print_report(record["label"], record["value"], record["limit"],difference,percent,status)
# ==========================================================================