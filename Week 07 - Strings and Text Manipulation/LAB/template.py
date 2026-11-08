"""
RECORD CHECK  -  my version
===========================

Name  : Robert OKonski
Lane  :   AI      
Date  : 08/11/2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """cleans and parses one status record"""
    line = raw_line.strip().lower()
    dataset_part, rest = line.split(",", 1)
    record = {"dataset": dataset_part.strip()}

    """Each field being separated, clean it, and convert its value to a number"""
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())
        
    return record

def status_of(rating):
 """Returns a status based on the survey rating."""
 if rating >= 100:
    return "OVER LIMIT"
 elif rating >= 90:
    return "WARNING"
 else:
    return "OK"
# ====================================================================== INPUT
raw_records = []
"""reads my record from the file"""
with open("survey_lines.txt") as f:
    for raw_line in f:
        raw_records.append(raw_line)
# =============================================================== PROCESS + OUTPUT
"""starts counter"""
flagged_count = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status =status_of(record["rating"])
    print(record, status)
    
    if status != "OK":
        flagged_count += 1

print("Records:", len(raw_records), "Flagged:", flagged_count)
# ==========================================================================

