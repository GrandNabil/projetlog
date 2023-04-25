import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


def dashboard(con):
    """
    Visualise les logs stockés dans la base de données.
    """
    logs = pd.read_sql_query('SELECT * FROM logs', con)

    # Graphique des niveaux de priorité
    counts = logs['priority'].value_counts()
    counts.plot(kind='bar', rot=0)
    plt.title('Nombre d\'entrées de log pour chaque niveau de priorité')
    plt.xlabel('Niveau de priorité')
    plt.ylabel('Nombre d\'entrées de log')

    # Affichage du graphique
    plt.show()
