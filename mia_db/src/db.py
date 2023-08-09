import psycopg2

db = psycopg2.connect(host='localhost', port='5432', dbname='mia_portfolio', user='postgres')