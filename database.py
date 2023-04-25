import sqlite3


def create_connection():
    """ 
        Connexion à la base de données.
    """
    con = None
    try:
        con = sqlite3.connect("logs.db")
    except sqlite3.Error as e:
        print(e)

    return con


def create_table(con):
    """ 
    Création de la table logs si elle n'existe pas déjà.
    """
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS logs(id INTEGER PRIMARY KEY, timestamp TEXT NOT NULL, hostname TEXT "
                    "NOT NULL, "
                    "appname TEXT NOT NULL, pid INTEGER NOT NULL, message TEXT NOT NULL)")
        cur.execute("ALTER TABLE logs ADD COLUMN priority TEXT")

        con.commit()
        print("La table 'log' a été créée avec succès.")
    except sqlite3.Error as e:
        print(e)


def insert_log(con, log):
    """
    Insertion de log dans la base de données.
    """
    cur = con.cursor()
    try:
        cur.execute('''
                INSERT INTO logs (timestamp, hostname, appname, pid, message, priority)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (log['timestamp'], log['hostname'], log['appname'], int(log['pid']), log['message'], log['priority']))
    except sqlite3.Error as e:
        print(e)


def select_logs(con):
    """
    Renvoie tous les logs de la base de données.
    """
    cur = con.cursor()
    try:
        return cur.execute('SELECT * FROM logs').fetchall()
    except sqlite3.Error as e:
        print(e)
