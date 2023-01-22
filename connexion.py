import psycopg2

# établissement de la connexion
conn = psycopg2.connect(
    host="hostname",
    database="database_name",
    user="username",
    password="password"
)

# création d'un curseur pour interagir avec la base de données
cursor = conn.cursor()

# exécution d'une requête SQL
cursor.execute("SELECT * FROM table_name")

# récupération des résultats
results = cursor.fetchall()

# parcours des résultats
for row in results:
    print(row)

# fermeture de la connexion
conn.close()
