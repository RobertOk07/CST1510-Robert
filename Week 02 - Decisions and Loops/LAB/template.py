"""
RECORD CHECK  -  my version
===========================

Name  : Robert Okonski
Lane  :    IT      
Date  : 01/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
lane_lable= ("IT")
hostname_name= input("What is your host name(or quit) : ")
gbused_storage= float(input(" How much GB did you use, Sir? : "))
gbtotal_storage= float(input(" HOw much GB did you use in Total, Sir : "))
overlimit_count= 0



# ================================================================== PROCESS
if ((gbused_storage/gbtotal_storage)* 100) >= 100:
    status= ("OVER LIMIT")
    overlimit_count += 1    
elif ((gbused_storage/gbtotal_storage)* 100) >= 90:
    status=("WARNING")
else:
    status=("OK")


  
    


# =================================================================== OUTPUT
print("=" * 30)
print("RECORD CHECK  : ",hostname_name)
print("=" * 30)
print("Used     : ",gbused_storage)
print("Total    : ",gbtotal_storage)
print(f"Free     : {gbtotal_storage - gbused_storage:>5.2f}")
print(f"Percent  : {(gbused_storage / gbtotal_storage) * 100:>5.2f}, %")
print("Status   : ",status)
print("Over limit : ",overlimit_count)
print("=" * 30)

# it took me, some trial and error to get the allignment right
# same goes for line 42, where to place the ":>5.2f" space funtion also took me trial and error to find out where the correct placement is.











# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
