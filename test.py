import os
import time

print(" Checking Network...\n")

response = os.system("ping 192.168.2.2")

if response == 0:
    print("\n Network is Stable")
else:
    print("\n Issue Detected!")
    print("Attempting Self-Healing...\n")
    
    time.sleep(2)
    
    # Simulated fix
    print("Restarting network interface...")
    time.sleep(2)
    
    print(" Issue Resolved (Simulated)")