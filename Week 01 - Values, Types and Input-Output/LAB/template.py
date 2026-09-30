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
#================================================================== Threshold
source_IP= input("Hello Sir, what is your source IP? : ")
failed_logins= float(input("Hello Sir, how many failed logins did you have?" ))
total_attempts= float(input("Hello Sir, how many total attempts did you have?"))

print("================================\nLane Check Cybersecurity\n================================")
print("My source IP is : ",source_IP)
print("Hello, i had : ",failed_logins, "today")
print("Hello, i had : ",total_attempts, "today")
print("=" * 30)

# ================================================================== Typical+Excellent
source_IP= input("Hello Sir, what is your source IP? : ")
failed_logins= float(input("Hello Sir, how many failed logins did you have?" ))
total_attempts= float(input("Hello Sir, how many total attempts did you have?"))
limitfortotalattemps_reached= input("failed_logins //3")

print("================================\nLane Check Cybersecurity\n================================")
print(f"My source IP is : ",source_IP)
print(f"Hello, i had : {failed_logins:>10.2f} failed logins")
print(f"Hello, i had : {total_attempts:>10.2f} total attempts")
print(f"The difference : {total_attempts-failed_logins:>+10.2f}")
print(f"The difference in percent: {(failed_logins/total_attempts)*100:>+10.2f}","%")
print(f"Limit for total failed login reached : {limitfortotalattemps_reached:>+10.2f},try again in 24H ")
print("=" * 30)

#in line 32-35 i used "":>10.2f" so make the numbers be in 2 decimal places and right aligned in 10 spaces
#for the Excellent i added the "+" to each difference here

#for the Excellent i added a function which, when a total number of failed login attempts is reached you will be locked out. 
#That is the idea, but how to actually make the program stop is unknown to me. But i hope the idea makes sense.
# i made 3 to be the limit.

# =================================================================== OUTPUT
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
