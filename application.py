import time
import RPi.GPIO as GPIO
import threading

# Regle la designation des GPIO en mode BOARD
GPIO.setmode(GPIO.BOARD)
# Desactive les warnings
GPIO.setwarnings(False)

# Definition des emplacements des LEDs.
LED_VERTE = 7
LED_JAUNE = 11
LED_ROUGE = 13
BOUTON = 37

# Definition des directions et de l'etat initial des LEDs
GPIO.setup(LED_VERTE, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_JAUNE, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_ROUGE, GPIO.OUT, initial=GPIO.LOW)

# Definition de la direction du bouton
GPIO.setup(BOUTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Definition de la variable qui va stocker le status du feu (ON/OFF)
feu_status = False


# Definition d'une fonction qui set l'activation ou non des LEDs
def etat_feux(etat_led_verte, etat_led_jaune, etat_led_rouge):
    if feu_status:
        GPIO.output(LED_VERTE, etat_led_verte)
        GPIO.output(LED_JAUNE, etat_led_jaune)
        GPIO.output(LED_ROUGE, etat_led_rouge)
    else:
        GPIO.output(LED_VERTE, GPIO.LOW)
        GPIO.output(LED_JAUNE, GPIO.LOW)
        GPIO.output(LED_ROUGE, GPIO.LOW)


# Definition de la fonction qui va écouter le bouton, et changer l'état du status du feu
def change_feu_status():
    global feu_status
    while True:
        if GPIO.input(BOUTON):
            print("Bouton appuyé")
            if feu_status:
                feu_status = False
            else:
                feu_status = True
            print(f"Status du feu: {str(feu_status)}")
            time.sleep(2)


# Definition de la fonction gère le feu lorsqu'il est allumé
def programme_feu():
    while True:
        etat_feux(GPIO.HIGH, GPIO.LOW, GPIO.LOW)
        time.sleep(7)
        etat_feux(GPIO.LOW, GPIO.HIGH, GPIO.LOW)
        time.sleep(1)
        etat_feux(GPIO.LOW, GPIO.LOW, GPIO.HIGH)
        time.sleep(7)

# Definition des threads, qui vont permettre d'executer les fonctions de façon asynchrone
a = threading.Thread(None, change_feu_status, None)
b = threading.Thread(None, programme_feu, None)

# Lancement des threads.
a.start()
b.start()