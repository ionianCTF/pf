# Micro Service That reads from a SQLITE db every 5 minutes and
# publishes through MQTT the results for Wifi and BLT
# Sends The number of unique devices and the number of returning devices (device recorded more than once in the last 5 min)
# For both Wifi and blt

import json
import sqlite3
import time

import paho.mqtt.publish as publish
import schedule

from consts import mqtt_broker_address, sensor_id, wifi_topic, clasic_bluetooth_topic, ble_bluetooth_topic

greeting = your_string_variable = """
Hail, mighty gods of Olympus, hear my call,
Bearer of tidings, I stand before you tall.
With nimble feet and wings unfurled,
I traverse realms to share the world.
"""
# Connect to an SQLite in-memory database
db_file = "./db/data.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()


def count_unique_and_returning_wifi(table_name):
    current_time = int(time.time())
    five_minutes_ago = current_time - 300
    # Count unique devices
    unique_devices = cursor.execute(
        f"SELECT COUNT(DISTINCT ssid) FROM {table_name} WHERE insertion_time >= ?",
        (five_minutes_ago,),
    ).fetchone()[0]

    # Count returning devices (devices recorded more than once in the last 5 minutes)

    returning_devices = cursor.execute(
        f"SELECT COUNT(*) FROM (SELECT ssid FROM {table_name} WHERE insertion_time >= ? GROUP BY ssid HAVING COUNT(*) > 1)",
        (five_minutes_ago,),
    ).fetchone()[0]

    return unique_devices, returning_devices


def count_unique_and_returning_bl(table_name):
    # Count unique devices
    current_time = int(time.time())
    five_minutes_ago = current_time - 300

    unique_devices_count = cursor.execute(
        f"SELECT COUNT(DISTINCT device_address) FROM {table_name} WHERE insertion_time >= ?",
        (five_minutes_ago,),
    ).fetchone()[0]

    # Count returning devices
    returning_devices_count = cursor.execute(
        f"SELECT COUNT(*) FROM (SELECT device_address FROM {table_name} WHERE insertion_time >= ? GROUP BY device_address HAVING COUNT(*) > 1)",
        (five_minutes_ago,),
    ).fetchone()[0]

    return unique_devices_count, returning_devices_count


# All the data (ble,classic,wifi) -> Returing (Past x time (hour, day, ...))
def main():
    # Greet The Gods
    #for line in greeting.split("\n"):
    #    print(line)

    try:
        # Count unique and returning devices for WiFi
        wifi_unique, wifi_returning = count_unique_and_returning_wifi("wifi_data")

        # Count unique and returning devices for Bluetooth
        bluetooth_unique, bluetooth_returning = count_unique_and_returning_bl(
            "ble_bluetooth_data"
        )

        # Count unique and returning devices for Bluetooth
        bluetooth_unique_cl, bluetooth_returning_cl = count_unique_and_returning_bl(
            "classic_bluetooth_data"
        )

        # Publish the results to the appropriate MQTT topic
        print("WiFi Devices:")
        print(f"Unique Devices: {wifi_unique}")
        print(f"Returning Devices: {wifi_returning}\n")

        print("Bluetooth Devices:")
        print(f"Unique Devices: {bluetooth_unique}")
        print(f"Returning Devices: {bluetooth_returning}\n")

        print("Bluetooth Devices Classic:")
        print(f"Unique Devices: {bluetooth_unique_cl}")
        print(f"Returning Devices: {bluetooth_returning_cl}\n")

        # Publish the results to the appropriate MQTT topics
        publish.single(wifi_topic,json.dumps([{"sensorId":sensor_id,"Unique_Devices": wifi_unique,"Returning_Devices":wifi_returning,"Timestamp":time.strftime("%Y-%m-%d %H:%M:%S")}]),hostname=mqtt_broker_address)
        publish.single(clasic_bluetooth_topic,json.dumps([{"sensorId":sensor_id,"Unique_Devices": bluetooth_unique_cl,"Returning_Devices":bluetooth_returning_cl,"Timestamp":time.strftime("%Y-%m-%d %H:%M:%S")}]),hostname=mqtt_broker_address)
        publish.single(ble_bluetooth_topic,json.dumps([{"sensorId":sensor_id,"Unique_Devices": bluetooth_unique,"Returning_Devices":bluetooth_returning,"Timestamp":time.strftime("%Y-%m-%d %H:%M:%S")}]),hostname=mqtt_broker_address)
    except Exception as e:
        print(f"Error during data retrieval: {str(e)}")


schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    try:
        time.sleep(1)
    except Exception as e:
        print(f"Error during BLE device discovery with pygatt: {str(e)}")
        pass
    
