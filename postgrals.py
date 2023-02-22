import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'root'
database = 'playlistsong'
port = 5432


conn = psycopg2.connect(hostname = hostname, username = username, password = password, database = database, port = port)
