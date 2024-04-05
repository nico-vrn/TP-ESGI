import subprocess

user = 'nicos'
password = 'password'
database = 'python'
host = '127.0.0.1'
query = "SELECT * FROM ma_table;"

command = f"mysql -h {host} -u{user} -p{password} -D {database} -e \"{query}\""

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

stdout, stderr = process.communicate()

if process.returncode == 0:
    print("Résultat de la requête :")
    print(stdout)
else:
    print("Erreur lors de l'exécution de la commande MySQL :")
    print(stderr)