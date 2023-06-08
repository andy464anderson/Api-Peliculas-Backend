import psycopg2

#creamos la funcion para conectarnos a la base de datos

def conectar():
    #creamos la conexion a la base de datos
    conn = psycopg2.connect(
        host="ec2-18-203-205-71.eu-west-1.compute.amazonaws.com",
        database="d4lap1mkcchg4o",
        user="wxdhivoapomzse",
        password="86fddfec4d5fa2cc95187612d100458298d5b2f6334d00224ca3222f9f17ed02"
    )
    #devolvemos la conexion
    return conn