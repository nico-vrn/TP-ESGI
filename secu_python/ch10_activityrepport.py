import subprocess
import matplotlib.pyplot as plt
import time

def recuperer_donnees_idle():
    result = subprocess.run(['sar', '1', '1'], capture_output=True, text=True)
    lines = result.stdout.split('\n')
    for line in lines:
        if "Average" in line and "all" in line:
            return float(line.split()[-1])

def appliquer_charge_cpu(duree=10):
    subprocess.Popen(['stress', '--cpu', '1', '--timeout', str(duree)])

donnees_idle = []

print("Application d'une charge de travail sur le serveur...")
appliquer_charge_cpu(10)

print("Collecte des données d'activité du serveur...")
for _ in range(12):  
    idle = recuperer_donnees_idle()
    if idle is not None:
        donnees_idle.append(idle)
    time.sleep(1)

plt.plot(donnees_idle, label='% Idle', marker='o', linestyle='-')
plt.xlabel('Intervalle de temps')
plt.ylabel('% Idle')
plt.title('Évolution de l\'activité du serveur au fil du temps')
plt.legend()

plt.savefig('activite_serveur.png')
print("Le graphique a été sauvegardé sous 'activite_serveur.png'")
