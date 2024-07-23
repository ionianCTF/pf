import random
import sqlite3
import time

# Connect to SQLite database file
db_file = "data.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute(
    """CREATE TABLE IF NOT EXISTS wifi_data
                (ssid TEXT, bssid TEXT, signal_strength REAL, capabilities TEXT, insertion_time TEXT)"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS classic_bluetooth_data
                (device_address TEXT, device_name TEXT, rssi REAL, insertion_time TEXT)"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS ble_bluetooth_data
                (device_address TEXT, device_name TEXT, rssi REAL, insertion_time TEXT)"""
)

conn.commit()


# Function to add fake Wi-Fi records
def add_fake_wifi_records(num_records):
    for _ in range(num_records):
        ssid = "FakeSSID4"  # Example SSID
        bssid = "00:11:22:33:44:54"  # Example BSSID
        signal_strength = random.uniform(-100, 0)
        capabilities = "WPA2"  # Example capabilities
        insertion_time = int(time.time())
        cursor.execute(
            """INSERT INTO wifi_data
                          (ssid, bssid, signal_strength, capabilities, insertion_time) VALUES (?, ?, ?, ?, ?)""",
            (ssid, bssid, signal_strength, capabilities, insertion_time),
        )
    conn.commit()


# Function to add fake classic Bluetooth records
def add_fake_classic_bluetooth_records(num_records):
    for _ in range(num_records):
        device_address = "00:11:22:33:44:65"  # Example device address
        device_name = "FakeDevice"  # Example device name
        rssi = random.uniform(-100, 0)
        insertion_time = int(time.time())
        cursor.execute(
            """INSERT INTO classic_bluetooth_data
                          (device_address, device_name, rssi, insertion_time) VALUES (?, ?, ?, ?)""",
            (device_address, device_name, rssi, insertion_time),
        )
    conn.commit()


# Function to add fake BLE Bluetooth records
def add_fake_ble_bluetooth_records(num_records):
    for _ in range(num_records):
        device_address = "00:12:22:33:44:55"  # Example device address
        device_name = "FakeDevice"  # Example device name
        rssi = random.uniform(-100, 0)
        insertion_time = int(time.time())
        cursor.execute(
            """INSERT INTO ble_bluetooth_data
                          (device_address, device_name, rssi, insertion_time) VALUES (?, ?, ?, ?)""",
            (device_address, device_name, rssi, insertion_time),
        )
    conn.commit()


# Add fake records
add_fake_wifi_records(5)
add_fake_classic_bluetooth_records(5)
add_fake_ble_bluetooth_records(5)

# Close the connection
conn.close()
