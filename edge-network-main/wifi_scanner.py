import time

import schedule
import sqlite3
import wifi_lib as WiFiScanner


def main():
    conn, cursor = WiFiScanner.create_database()
    # Enable Wi-Fi
    WiFiScanner.enable_wifi()
    # Discover WiFi devices
    WiFiScanner.scan(conn, cursor)
    


schedule.every().minute.do(main)

while True:
    schedule.run_pending()
    try:
        time.sleep(1)
    except Exception as e:
        print(f"Error during Wifi device discovery with pygatt: {str(e)}")
        pass
    
    
