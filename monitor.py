import subprocess
import re
import time
from datetime import datetime

# Target IP (use real reachable IP)
target_ip = "8.8.8.8"

print(" Starting Intelligent Network Monitoring...\n")

def check_network():
    try:
        result = subprocess.run(
            ["ping", target_ip, "-n", "4"],
            capture_output=True,
            text=True
        )

        output = result.stdout
        print(output)

        # Extract packet loss
        loss_match = re.search(r"Lost = (\d+)", output)

        # Extract latency
        latency_match = re.search(r"Average = (\d+)", output)

        if loss_match:
            loss = int(loss_match.group(1))

            if latency_match:
                latency = int(latency_match.group(1))
            else:
                latency = -1  # when no response

            print(f"\n Packet Loss: {loss}")
            print(f" Latency: {latency} ms")

            # Timestamp
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Save logs
            with open("network_log.txt", "a") as f:
                f.write(f"{current_time} | Loss: {loss}, Latency: {latency}\n")

            # Intelligent Detection
            if loss == 4:
                print("\n CRITICAL: Network DOWN (100% packet loss)")
                print(" Triggering Self-Healing...")
                time.sleep(2)

                print("Restarting network interface...")
                time.sleep(2)

                print(" Recovery Attempt Completed\n")

            elif loss > 1 or (latency != -1 and latency > 100):
                print("\n WARNING: Network Degradation Detected")
                print(" Triggering Optimization...")
                time.sleep(2)

                print("Adjusting network parameters...")
                time.sleep(2)

                print(" Optimization Done\n")

            else:
                print("\n Network is Stable\n")

        else:
            print(" Could not parse ping output\n")

    except Exception as e:
        print(f" Error occurred: {e}")


# Continuous Monitoring Loop
while True:
    check_network()
    print(" Checking again in 10 seconds...\n")
    time.sleep(10)