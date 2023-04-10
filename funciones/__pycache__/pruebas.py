import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def insertarre(tabla,idre,canhab,numpersonas,fechaini,fechafin,idusuario,idhabi):
    sentencia=f"INSERT INTO {tabla} VALUES ('{idre}','{canhab}','{numpersonas}','{fechaini}','{fechafin}','{idusuario}','{idhabi}')"
    print(sentencia)
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')

insertarre('tb_reserva',5,5,5,'29-03-2023','30-03-2023',19999,909)