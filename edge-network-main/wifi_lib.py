import json
import os
import utils
import sqlite3
import time
from scapy.sendrecv import sniff
from scapy.layers.dot11 import Dot11
from consts import wifi_interface, scan_duration

# # Function to create an SQLite in-memory database and table
# def create_database():
#     conn = sqlite3.connect("./db/data.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         """CREATE TABLE IF NOT EXISTS wifi_data (
#                         sensor_id TEXT,
#                         ssid TEXT,
#                         bssid TEXT,
#                         distance REAL,
#                         capabilities TEXT
#                         add insertion time
#                     )"""
#     )
#     conn.commit()
#     return conn, cursor
# def wifi_packet_handler(pkt, all_networks):
#     if pkt.haslayer(Dot11):
#         if pkt.type == 0:  # Management frame
#             if pkt.subtype == 8:  # Beacon frame
#                 ssid = pkt.info.decode("utf-8")
#                 bssid = pkt.addr2
#                 signal_strength = pkt.dBm_AntSignal
#                 capabilities = pkt.cap if hasattr(pkt, "cap") else "Unknown"
#                 all_networks.append(
#                     (
#                         utils.hash(bssid),
#                         utils.hash(ssid),
#                         utils.rssi_to_distance(signal_strength),
#                         capabilities,
#                     )
#                 )
#             elif pkt.subtype == 4:  # Probe Request frame
#                 ssid = pkt.info.decode("utf-8")
#                 if ssid == "":
#                     ssid = "Unknown"
#                 bssid = pkt.addr2
#                 signal_strength = pkt.dBm_AntSignal
#                 all_networks.append(
#                     (
#                         utils.hash(bssid),
#                         utils.hash(ssid),
#                         utils.rssi_to_distance(signal_strength),
#                         "Probe Request",
#                     )
#                 )
#             elif pkt.subtype == 5:  # Probe Response frame
#                 ssid = pkt.info.decode("utf-8")
#                 if ssid == "":
#                     ssid = "Unknown"
#                 bssid = pkt.addr2
#                 signal_strength = pkt.dBm_AntSignal
#                 capabilities = pkt.cap if hasattr(pkt, "cap") else "Unknown"
#                 all_networks.append(
#                     (
#                         utils.hash(bssid),
#                         utils.hash(ssid),
#                         utils.rssi_to_distance(signal_strength),
#                         f"Probe Response ({capabilities})",
#                     )
#                 )
# def enable_wifi():
#     # Set the interface to monitor mode
#     os.system(f"sudo ifconfig {wifi_interface} down")
#     os.system(f"sudo iwconfig {wifi_interface} mode monitor")
#     os.system(f"sudo ifconfig {wifi_interface} up")
# # Function to get Wi-Fi data using scapy
# def scan(conn, cursor):
#     all_networks = []
#     try:
#         # Use scapy's sniff function to capture Wi-Fi packets
#         print(f"Scanning WiFis for {scan_duration} seconds...")
#         sniff(
#             iface=wifi_interface,
#             prn=lambda pkt: wifi_packet_handler(pkt, all_networks),
#             store=0,
#             timeout=scan_duration,
#         )
#         # Remove duplicates based on BSSIDs
#         unique_networks = list(
#             {network[1]: network for network in all_networks}.values()
#         )
#         insertion_time = time.strftime("%Y-%m-%d %H:%M:%S")
#         cursor.executemany(
#             """INSERT INTO wifi_data (sensor_id, ssid, bssid, distance, capabilities, insertion_time)
#                VALUES (?, ?, ?, ?, ?, ?)""",
#             [
#                 (
#                     network[0],
#                     network[1],
#                     network[2],
#                     network[3],
#                     network[4],
#                     insertion_time,
#                 )
#                 for network in unique_networks
#             ],
#         )
#         # utils.save_to_csv_wifi(unique_networks)
#     except Exception as e:
#         print(f"Error during WiFi discovery: {str(e)}")
# Function to get Wi-Fi data using scapy
