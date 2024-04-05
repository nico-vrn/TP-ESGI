import signal
import time
import readchar

def handler(sig, frame):
    msg='\nVoulez-vous arretez ? (o/n)'
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'o':
        print("")
        exit(1)
    else:
        print(msgstop)

# Configuration de l'interception du signal SIGINT
signal.signal(signal.SIGINT, handler)

msgstop="\nAppuyez sur CTRL-C pour quitter."
print(msgstop)

# Boucle infinie pour maintenir le programme en cours d'exécution
while True:
    time.sleep(1)
