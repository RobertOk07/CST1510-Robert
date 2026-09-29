"""
RECORD CHECK  -  my version
===========================

Name  : Robert Dawid Okonski
Lane  :   Cyber      (delete two)
Date  : 29/09/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
#================================================================== INPUT
source_IP= input("Hello Sir, what is your source IP? : ")
failed_logins= float(input("Hello Sir, how many failed logins did you have?" ))
total_attempts= float(input("Hello Sir, how many total attempts did you have?"))

print("================================\nLane Check Cybersecurity\n================================")
print("My source IP is : ",source_IP)
print("Hello, i had : ",failed_logins, "today")
print("Hello, i had : ",total_attempts, "today")
print("=================================")

# ================================================================== PROCESS
source_IP= input("Hello Sir, what is your source IP? : ")
failed_logins= float(input("Hello Sir, how many failed logins did you have?" ))
total_attempts= float(input("Hello Sir, how many total attempts did you have?"))

print("================================\nLane Check Cybersecurity\n================================")
print(f"My source IP is : ",source_IP)
print(f"Hello, i had : {failed_logins:>10.2f} failed logins")
print(f"Hello, i had : {total_attempts:>10.2f} total attempts")
print(f"The difference : {total_attempts-failed_logins:>10.2f}")
print(f"The difference in percent: {(failed_logins-total_attempts)*100:>10.2f}","%")
print("==================================")

#in line 32-35 i used "":>10.2f" so make the numbers be in 2 decimal places and right alligned in 10 spaces






# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
