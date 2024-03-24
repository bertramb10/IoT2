from machine import Pin, deepsleep, ADC
from time import sleep
import dht
from adc_sub import ADC_substitute
import neopixel
import network
import espnow

# Initialiser objekter på pins
dht_sensor = dht.DHT11(Pin(32))
hw390_pin = Pin(33, Pin.IN)
adc_sub = ADC_substitute(34)  # Pinnummeret til ADC (f.eks. 34)
# create an input pin on pin #2, with a pull up resistor
pb = Pin(15, Pin.IN, Pin.PULL_UP)

# Antallet af pixels på NeoPixel-ringen
NUM_PIXELS = 12

# Initialiser NeoPixel-ringen
np = neopixel.NeoPixel(Pin(26), NUM_PIXELS)

# Definér ADC-spektret
max_adc_value = 3040  # ADC-værdi, der svarer til 100% batterikapacitet
min_adc_value = 1661  # ADC-værdi, der svarer til 0% batterikapacitet

# Definér maksimal og minimal batterikapacitet
max_battery_capacity = 100  # Maksimal batterikapacitet i procent
min_battery_capacity = 0    # Minimal batterikapacitet i procent

# Tærskelværdi for jordfugtighed
threshold = 4000

# Opsætning af ESP-NOW
station = network.WLAN(network.STA_IF)
station.active(True)

esp_now = espnow.ESPNow()
esp_now.active(True)

# Find MAC-adressen for modtageren (peer)
# dette er main esp mac adresse = 0C:B8:15:C5:26:C8
peer_mac_str = 'B0:A7:32:DE:16:B8'
peer_mac_bytes = bytes.fromhex(peer_mac_str.replace(':', ''))

# Tilføj modtageren (peer) til ESP-NOW
esp_now.add_peer(peer_mac_bytes)

# Funktion til at udføre DHT11-måling
def perform_dht11_measurement():
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    return temperature, humidity

# Funktion til at udføre HW390-måling
# Funktion til at udføre HW390-måling
def perform_hw390_measurement():
    moisture_sensor_pin = 33
    moisture_sensor = ADC(Pin(hw390_pin))
    threshold_value = 4000
    moisture_value = moisture_sensor.read()
    print(moisture_value)
    if moisture_value < threshold_value:
        return "Jorden er toer."
    else:
        return "Jorden er vaad."


# Funktion til at udføre batterimåling
def perform_battery_measurement():
    adc_value = adc_sub.read_adc()
    battery_capacity = ((adc_value - min_adc_value) / (max_adc_value - min_adc_value)) * (max_battery_capacity - min_battery_capacity)
    battery_capacity = min(max(battery_capacity, 0), 100)
    return battery_capacity

# Funktion til at gå i dvale
#def deep_sleep(minutes):
   # sleep_time = minutes * 60 * 1000
   # print("Going to sleep for", minutes, "minutes...")
   # deepsleep(sleep_time)

# Funktion til at sætte NeoPixel-ringen til rød farve
def set_pixels_to_red():
    if adc_sub.read_adc() >= 3020:  # Loop gennem pixel 0 til 5
        np[0] = (0, 255, 0)  # Rød farve (R, G, B)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        np[4] = (0, 255, 0)
        np[5] = (0, 255, 0)  # Rød farve (R, G, B)
        np[6] = (0, 255, 0)
        np[7] = (0, 255, 0)
        np[8] = (0, 255, 0)
        np[9] = (0, 255, 0)
        np[10] = (0, 255, 0)
        np[11] = (0, 255, 0)
    elif  3020 > adc_sub.read_adc() > 2906:
        np[0] = (0, 255, 0)  # Rød farve (R, G, B)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        np[4] = (0, 255, 0)
        np[5] = (0, 255, 0)  # Rød farve (R, G, B)
        np[6] = (0, 255, 0)
        np[7] = (0, 255, 0)
        np[8] = (0, 255, 0)
        np[9] = (0, 255, 0)
        np[10] = (0, 255, 0)
        np[11] = (0, 0, 0)
    elif 2906 > adc_sub.read_adc() > 2792:
        np[0] = (0, 255, 0)  # Rød farve (R, G, B)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        np[4] = (0, 255, 0)
        np[5] = (0, 255, 0)  # Rød farve (R, G, B)
        np[6] = (0, 255, 0)
        np[7] = (0, 255, 0)
        np[8] = (0, 255, 0)
        np[9] = (0, 255, 0)
        np[10] = (0, 0, 0)
        np[11] = (0, 0, 0)
    elif 2792 > adc_sub.read_adc() > 2678:
        np[0] = (0, 255, 0)  # Rød farve (R, G, B)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        np[4] = (0, 255, 0)
        np[5] = (0, 255, 0)  # Rød farve (R, G, B)
        np[6] = (0, 255, 0)
        np[7] = (0, 255, 0)
        np[8] = (0, 255, 0)
        np[9] = (0, 0, 0)
        np[10] = (0, 0, 0)
        np[11] = (0, 0, 0)
    elif 2678 > adc_sub.read_adc() > 2565:
        np[0] = (0, 255, 0)  # Rød farve (R, G, B)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        np[4] = (0, 255, 0)
        np[5] = (0, 255, 0)  # Rød farve (R, G, B)
        np[6] = (0, 255, 0)
        np[7] = (0, 255, 0)
        np[8] = (0, 0, 0)
        np[9] = (0, 0, 0)
        np[10] = (0, 0, 0)
        np[11] = (0, 0, 0)
    elif 2565 > adc_sub.read_adc() > 2451:
        np[0] = (0, 255, 0)  # Rød farve (R, G, B)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        np[4] = (0, 255, 0)
        np[5] = (0, 255, 0)  # Rød farve (R, G, B)
        np[6] = (0, 255, 0)
        np[7] = (0, 0, 0)
        np[8] = (0, 0, 0)
        np[9] = (0, 0, 0)
        np[10] = (0, 0, 0)
        np[11] = (0, 0, 0)
    elif  2451 > adc_sub.read_adc() > 2338:
        np[0] = (0, 255, 0)  # Rød farve (R, G, B)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        np[4] = (0, 255, 0)
        np[5] = (0, 255, 0)  # Rød farve (R, G, B)
        np[6] = (0, 0, 0)
        np[7] = (0, 0, 0)
        np[8] = (0, 0, 0)
        np[9] = (0, 0, 0)
        np[10] = (0, 0, 0)
        np[11] = (0, 0, 0)
    elif 2338 > adc_sub.read_adc() > 2224:
        np[0] = (0, 255, 0)  # Rød farve (R, G, B)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        np[4] = (0, 255, 0)
        np[5] = (0, 0, 0)  # Rød farve (R, G, B)
        np[6] = (0, 0, 0)
        np[7] = (0, 0, 0)
        np[8] = (0, 0, 0)
        np[9] = (0, 0, 0)
        np[10] = (0, 0, 0)
        np[11] = (0, 0, 0)
    elif 2224 > adc_sub.read_adc() > 2110:
        np[0] = (255, 0, 0)  # Rød farve (R, G, B)
        np[1] = (255, 0, 0)
        np[2] = (255, 0, 0)
        np[3] = (255, 0, 0)
        np[4] = (0, 0, 0)
        np[5] = (0, 0, 0)  # Rød farve (R, G, B)
        np[6] = (0, 0, 0)
        np[7] = (0, 0, 0)
        np[8] = (0, 0, 0)
        np[9] = (0, 0, 0)
        np[10] = (0, 0, 0)
        np[11] = (0, 0, 0)
    elif 2110 > adc_sub.read_adc() > 1996:
        np[0] = (255, 0, 0)  # Rød farve (R, G, B)
        np[1] = (255, 0, 0)
        np[2] = (255, 0, 0)
        np[3] = (0, 0, 0)
        np[4] = (0, 0, 0)
        np[5] = (0, 0, 0)  # Rød farve (R, G, B)
        np[6] = (0, 0, 0)
        np[7] = (0, 0, 0)
        np[8] = (0, 0, 0)
        np[9] = (0, 0, 0)
        np[10] = (0, 0, 0)
        np[11] = (0, 0, 0)
    elif 1996 > adc_sub.read_adc() > 1883:
        np[0] = (255, 0, 0)  # Rød farve (R, G, B)
        np[1] = (255, 0, 0)
        np[2] = (0, 0, 0)
        np[3] = (0, 0, 0)
        np[4] = (0, 0, 0)
        np[5] = (0, 0, 0)  # Rød farve (R, G, B)
        np[6] = (0, 0, 0)
        np[7] = (0, 0, 0)
        np[8] = (0, 0, 0)
        np[9] = (0, 0, 0)
        np[10] = (0, 0, 0)
        np[11] = (0, 0, 0)
    elif 1883 > adc_sub.read_adc() > 1769:
        np[0] = (255, 0, 0)  # Rød farve (R, G, B)
        np[1] = (0, 0, 0)
        np[2] = (0, 0, 0)
        np[3] = (0, 0, 0)
        np[4] = (0, 0, 0)
        np[5] = (0, 0, 0)  # Rød farve (R, G, B)
        np[6] = (0, 0, 0)
        np[7] = (0, 0, 0)
        np[8] = (0, 0, 0)
        np[9] = (0, 0, 0)
        np[10] = (0, 0, 0)
        np[11] = (0, 0, 0)
    elif 1769 > adc_sub.read_adc() > 1655:
        np[0] = (0, 0, 0)  # Rød farve (R, G, B)
        np[1] = (0, 0, 0)
        np[2] = (0, 0, 0)
        np[3] = (0, 0, 0)
        np[4] = (0, 0, 0)
        np[5] = (0, 0, 0)  # Rød farve (R, G, B)
        np[6] = (0, 0, 0)
        np[7] = (0, 0, 0)
        np[8] = (0, 0, 0)
        np[9] = (0, 0, 0)
        np[10] = (0, 0, 0)
        np[11] = (0, 0, 0)
    np.write()

# Funktion til at slukke NeoPixel-ringen
def set_pixels_to_black():
    for i in range(NUM_PIXELS):
        np[i] = (0, 0, 0)  # Sluk NeoPixel-ringen
    np.write()

# Uendelig løkke
# Uendelig løkke
while True:
    set_pixels_to_black()
    # Udfør DHT11-målinger
    temperature, humidity = perform_dht11_measurement()
    print(temperature, humidity)
    
    # Udfør HW390-målinger
    hw390_value = perform_hw390_measurement()
    print("HW-390 Value:", hw390_value)
    sleep(1)
    
    # Udfør batterimåling
    battery_capacity = perform_battery_measurement()
    print(battery_capacity)
    
    # Saml dataene i en streng
    data_to_send = "Temperatur: {}C, Humidity: {}%, HW390: {}, Battery: {}%".format(temperature, humidity, hw390_value, battery_capacity)

    
    # Send dataene via ESP-NOW til modtageren
    esp_now.send(peer_mac_bytes, data_to_send)
    sleep(5)
    # Aktivér NeoPixel-ringen, når trykknappen holdes nede
    button_state = pb.value()
    if button_state == 0:
        print("Trykknappen er holdt nede.")
        set_pixels_to_red()
        
        # Vent, indtil knappen er blevet sluppet igen
        while pb.value() == 0:
            pass  # Vent uden at gøre noget
    
        print("Trykknappen er blevet sluppet.")
        set_pixels_to_black()