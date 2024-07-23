import csv
import datetime
import hashlib
import json
import math


def rssi_to_distance(rssi, n=2):
    # Convert RSSI to distance (in meters)
    # n is the signal propagation constant or path-loss exponent
    # The value of n depends on the environmental factors
    return math.pow(10, (abs(rssi) - 59) / (10 * n))


def save_to_csv_blt(data):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"bluetooth_scan_results_{timestamp}.csv"
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["MAC Address", "SSID/Bluetooth Name", "Signal Strength/Distance"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(
                {
                    "MAC Address": item[0],
                    "SSID/Bluetooth Name": item[1],
                    "Signal Strength/Distance": 0,
                }
            )

    print("Data saved successfully.")


def save_to_csv_wifi(data):
    # Save unique results to CSV
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    csv_filename = f"wifi_scan_results_{timestamp}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["SSID", "BSSID", "Signal Strength", "Capabilities"])
        csv_writer.writerows(data)

    print(f"Unique results saved to {csv_filename}")


def hash(content):
    if content is not None and isinstance(content, str):
        # Create a hash object
        hash_object = hashlib.sha256()

        # Update the hash object with the string's bytes
        hash_object.update(content.encode())

        # Get the hashed value in hexadecimal format
        return hash_object.hexdigest()
    else:
        return ""
