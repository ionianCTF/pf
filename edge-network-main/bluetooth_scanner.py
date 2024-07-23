import sqlite3
import time

import schedule

import bluetooth_lib as BluetoothScanner

# Connect to SQLite database file
db_file = "./db/data.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()


def main():
    # Create tables if they don't exist
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS classic_bluetooth_data
                    (device_address TEXT, device_name TEXT, rssi INTEGER, insertion_time REAL)"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS ble_bluetooth_data
                    (device_address TEXT, device_name TEXT, rssi INTEGER, insertion_time REAL)"""
    )
    conn.commit()
    # Enable Bluetooth
    BluetoothScanner.enable_bluetooth()

    # Allow some time for devices to initialize (adjust as needed)
    time.sleep(5)

    # Discover Bluetooth devices
    BluetoothScanner.get_classic_data(conn, cursor)
    BluetoothScanner.get_ble_data(conn, cursor)


schedule.every().minute.do(main)

while True:
    schedule.run_pending()
    try:
        time.sleep(1)
    except Exception as e:
        print(f"Error during BLE device discovery with pygatt: {str(e)}")
        pass

