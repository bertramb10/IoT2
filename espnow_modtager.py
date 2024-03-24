import network
import espnow
from time import sleep
# A WLAN interface must be active to send()/recv()
station = network.WLAN(network.STA_IF)
station.active(True)

esp_now = espnow.ESPNow()
esp_now.active(True)

while True:
    host, msg = esp_now.recv()
    if msg:  # msg == None if timeout in recv()
        print("Data modtaget fra", host, ": ", msg)
        # Gør noget med de modtagne data her, f.eks. gem dem i en fil
        # Eksempel: gem dataene i en tekstfil
        with open("modtagne_data.txt", "a") as f:
            f.write(msg.decode() + "\n")
    else:
        print("Venter på at modtage data")
    
    # Tilføj en lille forsinkelse
    sleep(2)