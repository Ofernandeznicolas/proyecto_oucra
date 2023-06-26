"""Codigo para cargar en la Base de Datos
los feriados obtenidos en mi codigo -FeriadosApi
a traves de la clase DatosApi.
Pasandole unicamente como argumento el año"""

import sqlite3
from FeriadosApi import *

class BaseDatosFeriados:
    def __init__(self, conexion):
        
        self.conect = conexion
        self.conexion = sqlite3.connect(conexion)
        self.cursor = self.conexion.cursor()
        self.validacion = None
        self.fechas_a_cargar = None
    
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
            
    """ Defino un metodo para conectarme """       
    def conectar(self):
        self.conexion = sqlite3.connect(self.conect)
        
        self.cursor = self.conexion.cursor()
        
        return self.conexion, self.cursor    
       
    """Defino un metodo para ingresar los valores obtenidos
    a mi TablaFeriados"""
    def IngresarDatos(self):
           
        self.ValidoDatosIngresados()
        if self.validacion == True:
            print("Los resultados ya se han cargado anteriormente")
            self.conexion.close()
            return
        else: 
            self.conectar()
        
            for i in self.fechas_a_cargar:
                campo = list(i.keys())
                valores = list(i.values())
                Comando = f"INSERT INTO TablaFeriados ({','.join(campo)}) VALUES ({','.join(['?'] * len(valores))}) "
                self.cursor.execute(Comando, valores)
            
            self.conexion.commit()
            self.conexion.close()
    
    """ Metodo para validar si los resultados
    obtenidos no estan cargados previamente y sino
    cargar los que no se encuentren"""
    def ValidoDatosIngresados(self):
        
        self.conectar()
        self.cursor.execute("SELECT FechaFeriado FROM TablaFeriados")
        datos_actuales = [fecha[0] for fecha in self.cursor.fetchall()]
        print(datos_actuales)

        fechas_a_cargar = []
        for fecha in feriados_obtenidos:
            if fecha["FechaFeriado"] not in datos_actuales:
                fechas_a_cargar.append(fecha)
        
        if len(fechas_a_cargar) == 0:
            validacion = True
            self.validacion = validacion
            return self.validacion
        else:
            self.fechas_a_cargar = fechas_a_cargar
            return self.fechas_a_cargar
        

""" Utilizo una variable para asignarle la clase 
y le paso como argumento la direccion 
de la base de datos"""
basedatos = BaseDatosFeriados("C:/Users/ofern/OneDrive/Escritorio/Proyecto Oucra/proyecto_oucra/base de datos/BDtrabajoUocra.db") 

""" Utilizo una variable para asignarle la clase
para la obtencion de feriados, le paso como argumento
el año el cual deseo cargar"""
probar = DatosApi(2023)

""" Utilizo una variable para asignarle la funcion
.feriadosBD() correspondiente a la clase DatosApi
y asi obtener todos los feriados del año indicado
en la variable anterior"""
feriados_obtenidos = probar.feriadosBD()

"""Indico la orden de ingresar los datos obtenidos
en la base de datos"""
basedatos.IngresarDatos()

"""Imprimo los resultados de mi base de datos
correspondiente a tablaFeriados"""
#basedatos.ImprimirResultados()
