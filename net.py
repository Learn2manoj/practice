import os
from datetime import datetime

# List of devices to check – you can add more
devices = [
    "8.8.8.8",        # Google DNS
    "1.1.1.1",        # Cloudflare DNS
    "192.168.1.1",    # Router (example)
    "192.168.1.10"    # Local device (example)
]

status_report = []

print("Checking device status...\n")

for ip in devices:
    # Ping command: -c 1 = send only one ping
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    
    if response == 0:
        status = "ONLINE"
    else:
        status = "OFFLINE"
    
    print(f"{ip} → {status}")
    status_report.append(f"{ip} - {status}")

# Save report with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = "network_report.txt"

with open(filename, "w") as file:
    file.write("Network Device Status Report\n")
    file.write(f"Generated on: {timestamp}\n\n")
    for line in status_report:
        file.write(line + "\n")

print(f"\nReport saved as {filename}")
