import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Informations de connexion
email = "nlefranc@myges.fr"  # Assure-toi que c'est une adresse Outlook
password = "M&N14tmRct*ESGI"

# Création du message
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = "nlefranc@myges.fr"
msg['Subject'] = "Hello test"

# Corps du message
body = "CHAT POINT "
msg.attach(MIMEText(body, 'plain'))

# Connexion au serveur SMTP d'Outlook et envoi de l'email
try:
    server = smtplib.SMTP('smtp.office365.com', 587)  # Serveur SMTP d'Outlook
    server.starttls()  # Activation de la sécurité
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, msg['To'], text)
    server.quit()
    print("Email envoyé avec succès via Outlook !")
except Exception as e:
    print(f"Erreur lors de l'envoi de l'email : {e}")
