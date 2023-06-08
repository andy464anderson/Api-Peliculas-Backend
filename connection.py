import psycopg2

#creamos la funcion para conectarnos a la base de datos

def conectar():
    #creamos la conexion a la base de datos
    conn = psycopg2.connect(
        host="ep-super-thunder-933877-pooler.us-east-1.postgres.vercel-storage.com",
        database="verceldb",
        user="default",
        password="3PyJKHtRDS7m",
        sslmode="require"
    )
    #devolvemos la conexion
    return conn