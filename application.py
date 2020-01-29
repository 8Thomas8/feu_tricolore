import time
import RPi.GPIO as GPIO

# Regle la designation des GPIO en mode BOARD
GPIO.setmode(GPIO.BOARD)
# Desactive les warnings
GPIO.setwarnings(False)

# Definition des emplacements des LEDs.
LED_VERTE = 7
LED_JAUNE = 11
LED_ROUGE = 13

# Definition des directions et de l'etat initial des LEDs
GPIO.setup(LED_VERTE, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_JAUNE, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_ROUGE, GPIO.OUT, initial = GPIO.LOW)

# Definition d'une fonction qui set l'activation ou non des LEDs
def etat_feux(etat_led_verte, etat_led_jaune, etat_led_rouge):
    GPIO.output(LED_VERTE, etat_led_verte)
    GPIO.output(LED_JAUNE, etat_led_jaune)
    GPIO.output(LED_ROUGE, etat_led_rouge)

# Boucle infinie
while True:
    etat_feux(GPIO.HIGH, GPIO.LOW, GPIO.LOW)
    time.sleep(7)
    etat_feux(GPIO.LOW, GPIO.HIGH, GPIO.LOW)
    time.sleep(1)
    etat_feux(GPIO.LOW, GPIO.LOW, GPIO.HIGH)
    time.sleep(7)