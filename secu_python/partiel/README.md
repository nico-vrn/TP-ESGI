<h1 align="center">Partiel Python<h1>

<p>Ce repo est destiné à notre SIEM en python<br>
</p>

## Comment utiliser 
1. installer les requirements python demandé
```sh

```

2. Pour l'analyse et la détection exécuter le script app.py : 
```sh 
sudo python3 app.py
```
Flask est en mode débug, mais l'interface web fonctionne en localhost. 
Les boutons en haut ne fonctionne pas mais l'affichage des logs écris en db fonctionne.

3. Pour la gestion de fichier executer: 
```sh 
sudo python3 scripts/gestion_fichier.py 
```
Le script vous demandera le répertoire à analyser et en indiquera pour chaque fichier présent sa taille et son hash. 

4. Pour l'analyse forensic executer : 
```sh 
sudo python3 scripts/analyse_forensique.py
```
Le script demandera le fichier de log à tester (un exemple existe dans journal_test.log) et en sort les détections d'attaque.

## les fichiers
- analyse_forensique.py 
Sert à l'analyse forensique d'un fichier de log serveur.

- detection_connexions.py 
Sert à détecter les problème de sécurité. 

- gestion_fichiers.py 
Sert à donné la taille et le hash md5 de fichier contenu dans un dossier donné. 

- surveillance_reseau.py
Fait comme wireshark. 

- static/styles.css
Ancien fichier de style css (plus utilisé)

- templates/index.html
FIchier du dashboard

- app.py
Sert à lancer le serveur flask.

- journal_test.log
Sert à test le fichier d'analyse forensic.

- siem_logs.db 
Base de donnée utilisé pour les logs.