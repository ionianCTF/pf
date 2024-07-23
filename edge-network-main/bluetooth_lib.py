import os
import sqlite3
import time

# Libraries for classic Bluetooth
from bluetooth import discover_devices

# Libraries for BLE
from pygatt import GATTToolBackend

import utils
from consts import (
    bluetooth_interface,
    scan_duration,
)


def enable_bluetooth():
    # Set the interface to monitor mode
    #os.system(f"sudo hciconfig {bluetooth_interface} reset")
    os.system(f"sudo hciconfig {bluetooth_interface} down")
    os.system(f"sudo hciconfig {bluetooth_interface} up")
    os.system(f"sudo hciconfig {bluetooth_interface} piscan")


# Function to get classical Bluetooth data
def get_classic_data(conn, cursor):
    print("Scanning for classic Bluetooth devices...")
    bluetooth_data = []
    try:
        devices = discover_devices(scan_duration, lookup_names=True)
        for device in devices:
            print(device)
            device_address = utils.hash(device[0])
            device_name = device[1]
            rssi = 0
            insertion_time = float(time.time())
            cursor.execute(
                """INSERT INTO classic_bluetooth_data
                              (device_address, device_name, rssi, insertion_time) VALUES (?, ?, ?, ?)""",
                (device_address, device_name, rssi, insertion_time),
            )
    except Exception as e:
        print(f"Error during Classic Bluetooth device discovery with pybluez: {str(e)}")
    return bluetooth_data


# Function to get BLE data
def get_ble_data(conn, cursor):
    print("Scanning for BLE Bluetooth devices...")
    bluetooth_data = []
    try:
        # use pygatt
        backend = GATTToolBackend()
        backend.start()
        discovered_devices = backend.scan(timeout=scan_duration)
        for device in discovered_devices:
            print(device)
            device_address = utils.hash(device["address"])
            device_name = device.get("name", "Unknown Device")
            rssi = device.get("rssi", 0)
            insertion_time = float(time.time())
            cursor.execute(
                """INSERT INTO ble_bluetooth_data
                              (device_address, device_name, rssi,insertion_time) VALUES (?, ?, ?, ?)""",
                (device_address, device_name, rssi, insertion_time),
            )
            conn.commit()
    except Exception as e:
        print(f"Error during BLE device discovery with pygatt: {str(e)}")
    finally:
        backend.stop()
    return bluetooth_data
