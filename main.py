import logparser
from database import create_connection, create_table, insert_log
from dashboard import dashboard

# Chemin du fichier de logs
LOG_FILE_PATH = 'fontconfig.log'

# Connexion à la base de données
con = create_connection()

# Création de la table logs si elle n'existe pas
create_table(con)

# Parsing des logs
logs = logparser.parse(LOG_FILE_PATH)

# Insertion des logs dans la base de données
for log in logs:
    insert_log(con, log)

# Visualisation des logs
dashboard(con)
