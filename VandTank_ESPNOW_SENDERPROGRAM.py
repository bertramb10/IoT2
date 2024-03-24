from machine import Pin, PWM
from hcsr04 import HCSR04
from time import sleep
from neopixel import NeoPixel
import network
import espnow

# Definer pin-konstanter
ultrasonic_trigger_pin = 15  # Skal tilsluttes sensorens trigger-pin
ultrasonic_echo_pin = 2  # Skal tilsluttes sensorens echo-pin
ultrasonic_trigger_pin2 = 4  
ultrasonic_echo_pin2 = 0

pump_pin = 14  # Skal tilsluttes pumpens kontrol-pin
neopixel_pin = 26 # Skal tilsluttes Neopixel-ringens data-indgang 

# Definer tærskelværdier for start og stop af pumpen
start_threshold = 3  # Vandstand under denne værdi starter pumpen
stop_threshold = 11  # Vandstand over denne værdi stopper pumpen

# Initialiser ultralydssensorerne
ultrasonic = HCSR04(ultrasonic_trigger_pin, ultrasonic_echo_pin)
ultrasonic2 = HCSR04(ultrasonic_trigger_pin2, ultrasonic_echo_pin2)

# Initialiser pumpen
pump = PWM(Pin(pump_pin, Pin.OUT), freq=1, duty=0)  # Frekvens og dutycycle kan justeres

# Initialiser NeoPixel-ringen
num_pixels = 12  # Antal NeoPixel-LED'er i ringen
neopixel = NeoPixel(Pin(neopixel_pin, Pin.OUT), num_pixels)

# Opsætning af ESP-NOW
station = network.WLAN(network.STA_IF)
station.active(True)

esp_now = espnow.ESPNow()
esp_now.active(True)

# Find MAC-adressen for modtageren (peer)
peer_mac_str = 'B0:A7:32:DE:16:B8'
peer_mac_bytes = bytes.fromhex(peer_mac_str.replace(':', ''))

# Tilføj modtageren (peer) til ESP-NOW
esp_now.add_peer(peer_mac_bytes)

def measure_distance():
    # Funktion til at måle afstand ved hjælp af ultralydssensor
    return ultrasonic.distance_cm(), ultrasonic2.distance_cm()

def update_neopixel(water_level1, water_level2):
    # Funktion til at opdatere NeoPixel-ringen baseret på vandniveau
    for i in range(num_pixels):
        if water_level1 <= 2.59:
            # Grøn farve for vand
            neopixel[1] = (0, 0, 100)
            neopixel[2] = (0, 0, 100)
            neopixel[3] = (0, 0, 100)
            neopixel[4] = (0, 0, 100)
            neopixel[5] = (0, 0, 100)
        elif 2.6 < water_level1 <= 4.09:
            neopixel[1] = (0, 0, 100)
            neopixel[2] = (0, 0, 100)
            neopixel[3] = (0, 0, 100)
            neopixel[4] = (0, 0, 100)
            neopixel[5] = (0, 0, 0)  # Sluk for LED, hvis vandstanden ikke længere er i dette interval
        elif 4.1 < water_level1 <= 6.49:
            neopixel[1] = (0, 0, 100)
            neopixel[2] = (0, 0, 100)
            neopixel[3] = (0, 0, 100)
            neopixel[4] = (0, 0, 0)  # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[5] = (0, 0, 0)  # Sluk for LED, hvis vandstanden ikke længere er i dette interval
        elif 6.5 < water_level1 <= 8.89:
            neopixel[1] = (0, 0, 100)
            neopixel[2] = (0, 0, 100)
            neopixel[3] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[4] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[5] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
        elif 8.9 < water_level1 <= 11.49:
            neopixel[1] = (0, 0, 100)
            neopixel[2] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[3] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[4] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[5] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
        else:
            # Sluk for alle LED'er, hvis vandstanden ikke længere er i nogen af de definerede intervaller
            neopixel[i] = (0, 0, 0)

        if water_level2 <= 2.59:
            # Grøn farve for vand
            neopixel[11] = (227, 16, 178)
            neopixel[10] = (227, 16, 178)
            neopixel[9] = (227, 16, 178)
            neopixel[8] = (227, 16, 178)
            neopixel[7] = (227, 16, 178)
        elif 2.6 < water_level2 <= 4.09:
            neopixel[11] = (227, 16, 178)
            neopixel[10] = (227, 16, 178)
            neopixel[9] = (227, 16, 178)
            neopixel[8] = (227, 16, 178)
            neopixel[7] = (0, 0, 0)  # Sluk for LED, hvis vandstanden ikke længere er i dette interval
        elif 4.1 < water_level2 <= 6.49:
            neopixel[11] = (227, 16, 178)
            neopixel[10] = (227, 16, 178)
            neopixel[9] = (227, 16, 178)
            neopixel[8] = (0, 0, 0)  # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[7] = (0, 0, 0)  # Sluk for LED, hvis vandstanden ikke længere er i dette interval
        elif 6.5 < water_level2 <= 8.89:
            neopixel[11] = (227, 16, 178)
            neopixel[10] = (227, 16, 178)
            neopixel[9] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[8] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[7] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
        elif 8.9 < water_level2 <= 11.49:
            neopixel[11] = (227, 16, 178)
            neopixel[10] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[9] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[8] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
            neopixel[7] = (0, 0, 0)    # Sluk for LED, hvis vandstanden ikke længere er i dette interval
        else:
            # Sluk for alle LED'er, hvis vandstanden ikke længere er i nogen af de definerede intervaller
            neopixel[i] = (0, 0, 0)

    # Opdater NeoPixel-ringen
    neopixel.write()
    
def set_color(r, g, b):
    for i in range(num_pixels):
        neopixel[i] = (r, g, b)
    neopixel.write()

set_color(0, 0, 0)

try:
    while True:
        # Mål vandstanden
        sleep(1)
        water_level1, water_level2 = measure_distance()
        sleep(1)
        data_to_send = "Water Level 1: {}cm, Water Level 2: {}cm".format(water_level1, water_level2)

        # Send dataene via ESP-NOW til modtageren
        esp_now.send(peer_mac_bytes, data_to_send)
        
        # Tjek om pumpen skal startes eller stoppes
        if water_level1 < start_threshold:
            pump.duty(1023)  # Start pumpen med fuld styrke (kan justeres)
            print("Pumpen er startet.")
        elif water_level1 > stop_threshold:
            pump.duty(0)  # Stop pumpen
            print("Pumpen er stoppet.")

        # Udskriv vandstanden
        print("Vandstand sensor 1:", water_level1, "cm")
        print("Vandstand sensor 2:", water_level2, "cm")

        # Opdater NeoPixel-ringen
        update_neopixel(water_level1, water_level2)

        # Vent i et kort øjeblik, f.eks. 1 sekund, før du måler igen
        sleep(1)

except KeyboardInterrupt:
    # Stopper programmet, hvis der trykkes på Ctrl+C
    pump.duty(0)  # Sørg for at stoppe pumpen, når programmet afsluttes
    print("Program stoppet af brugeren.")
