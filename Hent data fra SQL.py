import polars as pl

host = "localhost"
user = "root"
password = "Velkommen25"
port = "port"
db_name = "db"

uri = "mysql://{0}:{1}@{2}:{3}/{4}".format(user,password,host,port,db_name)
query = "SELECT * FROM foo"
pl.read_database_uri(query=query, uri=uri)