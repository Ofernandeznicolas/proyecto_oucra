import sqlite3

from FeriadosApi import *


class baseDatosFeriados:
    def __init__(self, conexion):
        
        self.conect = conexion
        self.conexion = sqlite3.connect(conexion)
        self.cursor = self.conexion.cursor()


    """Imprimo resultados de una tabla - 
    Cambiar nombre de la tabla por self's que contengan las tablas de bd""" 
    def ImprimirResultados(self):
        self.conectar()
  
        self.cursor.execute("SELECT * FROM TablaFeriados")
        
        resultados = self.cursor.fetchall()
        
        for fila in resultados:
            print(fila)
        
        self.conexion.close()
    
    """Creo un metodo para verificar si me conecte
    correctamente con mi BD"""
    def ValidacionConexion(self):
        self.conectar()

        try:
            # realizo una consulta seleeccionando una tabla
            self.cursor.execute("SELECT * FROM TablaFeriados")

            # Obtengo los resultados
            resultados = self.cursor.fetchall()

            # corroboro si tengo los resultados.
            if resultados:
                print("Conexión exitosa. Se obtuvieron resultados.")
            else:
                print("Conexión exitosa. No se obtuvieron resultados.")

        except Exception as e:
            print("Error de conexión:", e)

        finally:
            # Cierro la conexion
            self.cursor.close()
            self.conexion.close()
            
    """ Defino un metodo para volver a conectarme """       
    def conectar(self):
        self.conexion = sqlite3.connect(self.conect)
        
        self.cursor = self.conexion.cursor()
        
        return self.conexion, self.cursor    
    
    
    """Defino un metodo para ingresar los valores obtenidos
    a mi TablaFeriados"""
    def IngresarDatos(self):
        
        self.conectar()
        
        for i in PruebaDiccionario2:
            campo = list(i.keys())
            valores = list(i.values())
            Comando = f"INSERT INTO TablaFeriados ({','.join(campo)}) VALUES ({','.join(['?'] * len(valores))}) "
            self.cursor.execute(Comando, valores)
        
        self.conexion.commit()
        self.conexion.close()
        

basedatos = baseDatosFeriados("C:/Users/ofern/OneDrive/Escritorio/Proyecto Oucra/proyecto_oucra/base de datos/BDtrabajoUocra.db") 


probar = datosApi(2022)

PruebaDiccionario2 = probar.feriadosBD() 

basedatos.ImprimirResultados()