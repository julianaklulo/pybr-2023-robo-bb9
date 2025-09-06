import time
import network

SSID = ""
PASSWORD = ""

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while wlan.isconnected() is False:
    print("Waiting for connection...")
    time.sleep(1)

print("Connection successful")
print("IP: ", wlan.ifconfig()[0])
